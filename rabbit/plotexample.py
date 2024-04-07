import matplotlib.pyplot as plt
import numpy as np
import time
import serial

plt.ion()


class DynamicUpdate():
    # Suppose    we know the x range
    min_x = 0
    max_x = 100

    def on_launch(self):
        self.serial = serial.Serial('COM3', 9600)
        self.serial.xonxoff = 1
        # Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([], [])
        self.lines2, = self.ax.plot([], [])
        self.integral, = self.ax.plot([], [])
        # Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        # self.ax.set_xlim(self.min_x, self.max_x)
        # Other stuff
        self.ax.grid()
        self.xdata = []
        self.ydata = []
        self.ydata2 = []
        self.y_integral = []

    def on_running(self):
        # Update data (with the new _and_ the old points)
        self.lines.set_xdata(self.xdata)
        self.lines.set_ydata(self.ydata)
        self.lines2.set_xdata(self.xdata)
        self.lines2.set_ydata(self.ydata2)
        self.integral.set_xdata(self.xdata)
        self.integral.set_ydata(self.y_integral)
        # Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        # We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    # Example
    def __call__(self):
        self.on_launch()
        # counter = 0
        for x in np.arange(0, 60000):
            # counter += 1
            time.sleep(0.001)
            self.serial.readline()
            if x % 100 == 0:
                # print(int(s.readline()[:-2]))
                self.xdata.append(x / 1000.0)
                self.ydata.append(int(self.serial.readline()[:-2]))
                self.ydata2.append(int(self.y_derivative()))
                self.integrate()
                self.on_running()
        # for x in np.arange(0,10,0.5):
        #         #     self.xdata.append(x)
        #         #     self.ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
        #         #     self.on_running()
        #         #     time.sleep(1)
        return self.xdata, self.ydata

    def y_derivative(self):
        if len(self.ydata) > 1:
            return (self.ydata[-1] - self.ydata[-2]) / (self.xdata[-1] - self.xdata[-2]) / 10
        else:
            return 0

    def integrate(self):
        if len(self.ydata) > 1:
            return self.y_integral.append(self.y_integral[-1] + abs((self.ydata[-1] - self.ydata[-2]) * (self.xdata[-1] - self.xdata[-2])))
            # return abs((self.ydata[-1] - self.ydata[-2])*(self.xdata[-1]-self.xdata[-2]))/10
        else:
            self.y_integral.append(0)


d = DynamicUpdate()
d()
