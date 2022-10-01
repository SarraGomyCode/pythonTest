import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.yatra.com/")
         driver.maximize_window()
         new_link = driver.find_element(By.XPATH,"//img[@alt='Upto 13% OFF (max. Rs.10,000) + No Cost EMI on 3 or 6 months']")
         new_link.click()
         time.sleep(4)
         handle_windows  = driver.current_window_handle
         print(handle_windows)
         all_windows = driver.window_handles
         print(all_windows)
         for current_window in all_windows:
             if current_window != handle_windows:
                 driver.switch_to.window(current_window)
                 driver.find_element(By.XPATH,"//span[normalize-space()='Company Information']").click()
                 time.sleep(4)
                 driver.close()
                 break

         driver.switch_to.window(handle_windows)
         new_link.click()


selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()