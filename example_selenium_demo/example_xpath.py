import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.yatra.com/")
         driver.maximize_window()
         lista = driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
         print(lista)
         time.sleep(4)

selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()