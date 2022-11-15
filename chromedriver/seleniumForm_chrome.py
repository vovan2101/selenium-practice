from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time



options = webdriver.ChromeOptions()


driver = webdriver.Chrome(
     executable_path='C:\\Users\\vovae\\Documents\\selenium-practice\\chromedriver\\chromedriver.exe',
      options=options,
)

try:

    driver.get('https://vk.com/')
    time.sleep(2)
    
    email_input = driver.find_element(by=By.ID, value='index_email')
    email_input.send_keys('89141943078')
    time.sleep(2)

    login_button_email = driver.find_element(by=By.CLASS_NAME, value='VkIdForm__button').click()
    time.sleep(2)

    password_input = driver.find_element(by=By.CLASS_NAME, value='vkc__TextField__input')
    password_input.send_keys('V89242093999v')
    time.sleep(2)

    login_button_password = driver.find_element(by=By.CLASS_NAME, value='vkuiButton').click()
    time.sleep(10)

except Exception:
    print(Exception)

finally:
    driver.close()
    driver.quit()