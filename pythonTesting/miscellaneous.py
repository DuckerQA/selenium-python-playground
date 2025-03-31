import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#config
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
driver.get_screenshot_as_file("screenshot.png")
time.sleep(2)

driver.quit()