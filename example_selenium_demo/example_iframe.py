import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
         driver.maximize_window()
         driver.switch_to.frame(driver.find_element(By.ID,("iframeResult")))
         time.sleep(4)
         driver.switch_to.frame(0)
         driver.find_element(By.XPATH,"//a[@class='w3-button tut-button']").click()


selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()