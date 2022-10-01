import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.yatra.com/")
         driver.maximize_window()
         lista = driver.find_elements(By.TAG_NAME,"a")
         for i in lista:
              print(i.text)
         time.sleep(4)

selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()