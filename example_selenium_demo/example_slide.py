import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class SeleniumDemoExample :
    def selenium_first_demo (self):
         driver = webdriver.Chrome()
         driver.get("https://www.snapdeal.com/products/mens-footwear-sports-shoes?sort=plrty")
         driver.maximize_window()
         left_slide = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
         actions = ActionChains (driver)
         #actions.drag_and_drop_by_offset(left_slide, 60, 0).perform()
         #actions.click_and_hold(left_slide).pause(1).move_by_offset(60, 0).release().perform()
         actions.move_to_element(left_slide).pause(1).click_and_hold(left_slide).move_by_offset(60,0).release().perform()
         time.sleep(4)
         right_slide = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
         actions.drag_and_drop_by_offset(right_slide, -60, 0).perform()
         time.sleep(4)



selenium_first_example = SeleniumDemoExample()
selenium_first_example.selenium_first_demo()