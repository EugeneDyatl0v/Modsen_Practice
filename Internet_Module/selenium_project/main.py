from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chromedriver_path = '/home/eugenedyatlov/work/Modsen_Practice/Internet_Module/selenium_project/chromedriver'

options = Options()
options.headless = False

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.google.com')

# Работа с LocalStorage
driver.execute_script("localStorage.setItem('key', 'value');")
value = driver.execute_script("return localStorage.getItem('key');")
print(f"LocalStorage value: {value}")
driver.execute_script("localStorage.removeItem('key');")
value = driver.execute_script("return localStorage.getItem('key');")
print(f"LocalStorage value after removal: {value}")

# Работа с Cookie
driver.add_cookie({'name': 'cookie_key', 'value': 'cookie_value'})
cookie = driver.get_cookie('cookie_key')
print(f"Cookie value: {cookie['value']}")
driver.delete_cookie('cookie_key')
cookie = driver.get_cookie('cookie_key')
print(f"Cookie value after deletion: {cookie}")

driver.quit()
