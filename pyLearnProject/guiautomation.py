import pyautogui, time

# screenResolution = pyautogui.size()
#
# print(screenResolution)
#
# print(screenResolution[0])
# print(screenResolution[1])
# # named tuples
# print(screenResolution.width)
# print(screenResolution.height)
#
# # Move to exact position
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=2)
#     pyautogui.moveTo(200, 100, duration=2)
#     pyautogui.moveTo(200, 200, duration=2)
#     pyautogui.moveTo(100, 200, duration=2)
#
# # Move to relative position
# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25) #right
#     pyautogui.move(0, 100, duration=0.25) #down
#     pyautogui.move(-100, 0, duration=0.25) #left
#     pyautogui.move(0, -100, duration=0.25) #up

# Get current mouse position - named tuple
# print(pyautogui.position())
#
# # Click
# pyautogui.click(10, 5, button='left')
# pyautogui.click(10, 5, button='middle')
# pyautogui.click(10, 5, button='right')

# # Dragging - Drawing in gimp
time.sleep(5)
pyautogui.click()
distance = 300
change = 50

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5) # Move right
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.5)  # Move down
    pyautogui.drag(-distance, 0, duration=0.5)  # Move left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.5)  # Move up
