import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://jqueryui.com/droppable/")
         driver.maximize_window()
         driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[contains(@class,'demo-frame')]"))
         drag_element = driver.find_element(By.ID,"draggable")
         drop_element = driver.find_element(By.ID, "droppable")
         actions = ActionChains (driver)
         actions.drag_and_drop_by_offset(drag_element,30,20).perform()
         #actions.drag_and_drop(drag_element,drop_element).perform()
         time.sleep(4)

selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()