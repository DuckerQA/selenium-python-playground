import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#when VPN, locally chrome or some other issues ?
# service_obj = Service("../chromedriver")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)









time.sleep(1)
