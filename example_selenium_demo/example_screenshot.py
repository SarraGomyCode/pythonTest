import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
         driver.maximize_window()
         screenshot_example = driver.find_element(By.ID,"login-continue-btn")
         screenshot_example.screenshot(".\\test.png")
         screenshot_example.click()
         time.sleep(4)
         driver.get_screenshot_as_png()
         driver.save_screenshot(".\\sarra.png")

selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()