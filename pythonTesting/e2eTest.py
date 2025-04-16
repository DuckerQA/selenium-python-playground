import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#config
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(5)
tested_device = "Blackberry"

driver.get("https://rahulshettyacademy.com/angularpractice/")

#redirect to shop page
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
available_devices = driver.find_elements(By.CSS_SELECTOR, 'app-card-list app-card')

for card in available_devices:
    title = card.find_element(By.CSS_SELECTOR, 'h4.card-title')
    if title.text == tested_device:
        button = card.find_element(By.CSS_SELECTOR, '.btn-info')
        button.click()

driver.execute_script("""
    var span = document.querySelector('.nav-link .sr-only');
    if (span) span.remove();
""")
checkout_control = driver.find_element(By.CSS_SELECTOR, '#navbarResponsive a.nav-link')
checkout_text = checkout_control.text.strip()

assert checkout_text == 'Checkout ( 1 )'
checkout_control.click()

assert driver.find_element(By.CSS_SELECTOR, 'tr td:nth-child(1) .media-body h4.media-heading').text == tested_device
driver.find_element(By.CSS_SELECTOR, '.btn-success').click()


driver.find_element(By.CSS_SELECTOR, '#country').send_keys("pol")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.suggestions')))
driver.find_element(By.CSS_SELECTOR, '.suggestions li a').click()
driver.find_element(By.CSS_SELECTOR, 'label[for="checkbox2"]').click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
alert = driver.find_element(By.CSS_SELECTOR, '.alert.alert-success')
alert_text = alert.text.strip().replace('×', '').strip()
assert alert_text == "Success! Thank you! Your order will be delivered in next few weeks :-)."
driver.quit()
