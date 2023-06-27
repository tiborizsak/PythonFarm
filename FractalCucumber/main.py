import time
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

opts = FirefoxOptions()
#opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

while True:
    browser.get("http://versiona.hu/")

    # time.sleep(5)
    #
    # for y in range(1, 5):
    #     browser.find_element(By.XPATH, '//html/body/header/div/div/div/div[2]/nav/div/ul/li[' + str(y) + ']/a').click()
    #     time.sleep(5)

    #browser.close()

    time.sleep(1625)
    browser.quit()
