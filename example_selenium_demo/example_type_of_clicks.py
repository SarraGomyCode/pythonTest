import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://demo.guru99.com/test/simple_context_menu.html")
         driver.maximize_window()
         right_click = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
         actions = ActionChains (driver)
         actions.context_click(right_click).perform()
         double_click = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
         actions.double_click(double_click).perform()


selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()