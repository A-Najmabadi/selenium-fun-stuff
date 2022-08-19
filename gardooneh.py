import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def random_email():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str_1 = ''.join(random.choice(letters) for i in range(8))
    result_str_2 = ''.join(random.choice(letters) for i in range(5))
    r_email = result_str_1 + '@' + result_str_2 + '.' + 'comeo'
    return r_email

driver = webdriver.Firefox()
driver.get('https://www.daneshjooyar.com/landing/gardooneh/')

e_box = driver.find_element(By.CLASS_NAME, 'wof-input')
e_box.send_keys(random_email())
sleep(5)

btn = driver.find_element(By.CSS_SELECTOR, '.wof-color-2 > span')
btn.click()
sleep(10)

code = driver.find_element(By.CSS_SELECTOR, '.wof-form-wrapper > input')
print(code.get_attribute('value'))
# print(code.text)


