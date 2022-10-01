import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.yatra.com/")
         driver.maximize_window()
         departure_destination = driver.find_element(By.ID,"BE_flight_origin_city")
         departure_destination.click()
         departure_destination.send_keys("New Delhi")
         departure_destination.send_keys(Keys.ENTER)

         arrival_destination = driver.find_element(By.ID,"BE_flight_arrival_city")
         arrival_destination.click()
         arrival_destination.send_keys("New")
         arrival_destination.send_keys(Keys.ENTER)

         arrival_destination_list = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]//li")
         print (len(arrival_destination_list))
         for result in arrival_destination_list :
              print(result.text)
              if "New York (JFK)" in result.text :
                   result.click()
                   time.sleep(4)
                   break
         driver.find_element(By.ID,"BE_flight_origin_date").click()

         all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
         for date in all_dates :
              if date.get_attribute(data-date) == "27/09/2022":
                   date.click()
                   time.sleep(4)
                   break



selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()