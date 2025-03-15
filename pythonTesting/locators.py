import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("RandomName")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Admin1")
driver.find_element(By.ID, "exampleCheck1").click()
# driver.find_element(By.ID, "exampleFormControlSelect1").
driver.find_element(By.XPATH, "//input[@type='radio' and @value='option2']").click()
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys("Hello Again")
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()

time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success" in message
driver.close()