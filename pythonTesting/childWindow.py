import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows_opened = driver.window_handles

driver.switch_to.window(windows_opened[1])
assert driver.title == 'New Window'
driver.close()

driver.switch_to.window(windows_opened[0])
assert driver.title == 'The Internet'