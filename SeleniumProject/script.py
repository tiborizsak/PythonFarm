from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def open_webpage(url):
    # Setup the Chrome driver
    # Specify the path to chromedriver if it's not in the PATH
    service = Service(executable_path='/home/tizsak/.wdm/drivers/chromedriver/linux64/127.0.6533.72/chromedriver-linux64/chromedriver')
    chrome_options = webdriver.ChromeOptions()

    # Initialize the driver with the specified service
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the URL
    driver.get(url)

    # Optionally, keep the browser open for a certain time or until a condition
    input("Press Enter to continue...")  # Keeps the browser open until user interaction

    # Close the browser
    driver.quit()

# URL to be opened
url = "https://syslog-ng.github.io/"

# Call the function with the URL
open_webpage(url)
