from selenium import webdriver
from time import sleep

driver = webdriver.Firefox() # opens FireFox
driver.get('https://google.com') # Goes to Google.com

sleep(5) # waits 5 seconds in Google.com
driver.quit() # closes the FireFox
