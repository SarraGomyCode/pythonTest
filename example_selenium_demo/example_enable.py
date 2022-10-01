import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://training.openspan.com/login")
         driver.maximize_window()
         driver.implicitly_wait(10)


selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()