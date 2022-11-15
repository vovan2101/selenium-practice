# from selenium import webdriver
import time
from seleniumwire import webdriver
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password


user_agents_list = [
    'hello_world',
    'best_of_the_best',
    'python_today'
]

useragent =  UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.random}')


proxy_options = {
    'proxy': {
        'https': f'http://{login}:{password}@138.128.91.65:8000'
    }
}

# driver = webdriver.Chrome(
#     executable_path='C:\\Users\\vovae\\Documents\\selenium-practice\\chromedriver\\chromedriver.exe',
#      options=options,
# )

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vovae\\Documents\\selenium-practice\\chromedriver\\chromedriver.exe',
     seleniumwire_options=proxy_options
)


try:

    driver.get('https://2ip.ru')
    time.sleep(5)

except Exception:
    print(Exception)

finally:
    driver.close()
    driver.quit()