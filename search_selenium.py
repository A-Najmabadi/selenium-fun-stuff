from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox() # opens FireFox
driver.get('https://google.com') # Goes to Google.com

search_element = driver.find_element(By.NAME, 'q') # finds search-box on Google.com
search_element.send_keys('Selenium') # types <Selenium> in search-box
search_element.send_keys(Keys.ENTER) # googles <Selenium> by entering


sleep(5) # waits 5 seconds in Google.com
driver.quit() # closes the FireFox