import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SeleniumDemoExample :
    def selenium_first_demo(self):
         driver = webdriver.Chrome()
         driver.get("https://training.openspan.com/login")
         driver.maximize_window()
         driver.implicitly_wait(10)
         driver.find_element(By.ID,"user_name00").send_keys("sarra")
         driver.find_element(By.ID,"user_pass").send_keys("sarra@test.com")



selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()