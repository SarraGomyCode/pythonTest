import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SeleniumDemoExample :
    def selenium_first_demo(self):
         driver = webdriver.Chrome()
         driver.get("https://www.salesforce.com/fr/form/signup/freetrial-sales-pe/?d=70130000000EqoP")
         driver.maximize_window()
         dropdown_list = driver.find_element(By.NAME,"CompanyEmployees")
         select_list = Select(dropdown_list)
         select_list.select_by_index(1)
         time.sleep(4)
         select_list.select_by_value("3")
         time.sleep(4)
         select_list.select_by_visible_text("100 à 499 employés")
         time.sleep(4)

selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()