import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.yatra.com/")
         driver.maximize_window()
         login = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
         actions = ActionChains (driver)
         actions.move_to_element(login).perform()
         driver.find_element(By.ID,"signInBtn").click()


selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()