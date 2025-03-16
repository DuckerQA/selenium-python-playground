import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("seleniummateo@indigobook.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("NewPasswordHello123")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("NewPasswordHello123")
driver.find_element(By.XPATH, '//button[text()="Save New Password"]').click()




time.sleep(5)