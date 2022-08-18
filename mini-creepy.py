from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep
import sqlite3 as sql

driver = webdriver.Firefox() # opens FireFox
driver.get('https://github.com') # goes to github.com
sleep(5)

a_elements = driver.find_elements(By.TAG_NAME, 'a') # find all of <a> Tags in github.com


conn = sql.connect('github.db') # creating database and connect to it
curs = conn.cursor() # creating a cursor to move on database
curs.execute(""" CREATE TABLE Github(NAME TEXT, LINK TEXT) """) # creating table

# import info to database
for a_tag in a_elements:
    name = a_tag.text
    link = a_tag.get_attribute('href')
    curs.execute('INSERT INTO Github VALUES (?, ?)', (name, link))
conn.commit() # commit changes

conn.close()  # closes from database 
driver.quit() # closes FireFox