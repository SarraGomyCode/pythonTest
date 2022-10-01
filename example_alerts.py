import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
         driver.maximize_window()
         driver.switch_to.frame(driver.find_element(By.ID,("iframeResult")))
         time.sleep(4)
         driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
         driver.switch_to.alert.accept()


selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()