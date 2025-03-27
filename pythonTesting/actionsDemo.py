import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.CSS_SELECTOR, '#mousehover')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Top')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()

