import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) #find_elements ignores implicity_wait that's why sleep here
products = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
assert len(products) > 0
for product in products:
    product.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(5) p.amount')
final_price = 0
for price in prices:
    final_price += int(price.text)

print(final_price)
assert int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) == final_price


driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
promo_info = driver.find_element(By.CSS_SELECTOR, '.promoInfo')
print(promo_info.text)
assert promo_info.text.strip() == "Code applied ..!"

#Disccount check - dynamic version
discount = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text.strip('%')
discount_as_number = int(discount) / 100
price_after_discount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(final_price, 'Final Price without discount')
print(discount_as_number, 'discount as %')
print(price_after_discount, 'Price after discount')
assert float(price_after_discount) == final_price * (1 - discount_as_number)

time.sleep(2)





