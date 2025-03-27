import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#config
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, '.blinkingText').click()

windows_opened1 = driver.window_handles

driver.switch_to.window(windows_opened1[1])
email_text = driver.find_element(By.CSS_SELECTOR, "a[href='mailto:mentor@rahulshettyacademy.com']").text
driver.close()
driver.switch_to.window(windows_opened1[0])


driver.find_element(By.ID, 'username').send_keys(email_text)
driver.find_element(By.ID, 'password').send_keys('learning')
driver.find_element(By.ID, 'signInBtn').click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))

assert driver.find_element(By.CSS_SELECTOR, '.alert.alert-danger.col-md-12').text == 'Incorrect username/password.'


