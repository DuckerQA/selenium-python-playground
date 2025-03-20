import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(8)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) #find_elements ignores implicity_wait that's why sleep here
products = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
assert len(products) > 0
for product in products:
    product.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
promo_info = driver.find_element(By.CSS_SELECTOR, '.promoInfo')
print(promo_info.text)
# assert promo_info == "Code applied ..!"applied
time.sleep(2)





