import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sqlite3 as sql

def random_email():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str_1 = ''.join(random.choice(letters) for i in range(8))
    result_str_2 = ''.join(random.choice(letters) for i in range(5))
    result_str_3 = ''.join(random.choice(letters) for i in range(4))
    r_email = result_str_1 + '@' + result_str_2 + '.' + result_str_3
    return r_email

def get_takhfif():
    conn = sql.connect('Codes.db')
    curs = conn.cursor()
    curs.execute('SELECT Code FROM Takhfif',)
    data = curs.fetchall()
    conn.close()

    if data:
        return data
    else:
        return False      

driver = webdriver.Firefox()
conn = sql.connect('Codes.db')
curs = conn.cursor()
curs.execute(""" CREATE TABLE IF NOT EXISTS Takhfif (Number INTEGER PRIMARY KEY NOT NULL, Email TEXT, Code TEXT) """)

for _ in range(5):
    driver.get('https://www.daneshjooyar.com/landing/gardooneh/')

    r_email = random_email()
    e_box = driver.find_element(By.CLASS_NAME, 'wof-input')
    e_box.send_keys(r_email)
    sleep(3)

    btn = driver.find_element(By.CSS_SELECTOR, '.wof-color-2 > span')
    btn.click()
    sleep(10)

    code = driver.find_element(By.CSS_SELECTOR, '.wof-form-wrapper > input')
    value = code.get_attribute('value')

    flag = True
    records = get_takhfif()
    if records != False:
        for record in records:
            if record[0] == value:
                flag = False
    
    if flag == True:
        curs.execute('INSERT INTO Takhfif (Email, Code) VALUES (?, ?)', (r_email, value))
         
conn.commit()
conn.close()

    