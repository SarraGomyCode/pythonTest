from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path = r'C:\Users\sayari\Desktop\sarra\pythonTest\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.lovehomeswap.com/blog/latest-news/the-50-most-visited-tourist-attractions-in-the-world')
driver.implicitly_wait(10)
driver.execute_script("window.scrollBy(0,3000)","")
careers_element = driver.find_element(By.LINK_TEXT, 'Careers')
driver.execute_script("arguments[0].scrollIntoView();",careers_element)
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1
driver.find_element(By.LINK_TEXT ,'Login').click()
wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
wait.until(EC.title_is("Login | Love Home Swap"))
email_element = driver.find_element(By.ID,'email')
email_element.send_keys("sarra@gmail.com")
password_element = driver.find_element(By.ID,'password')
email_element.send_keys("123456")
connexion_element = driver.find_element(By.TAG_NAME,'button')
connexion_element.click()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

