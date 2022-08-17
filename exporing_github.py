from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox() # opens the FireFox
driver.get('https://github.com/') # Goes to github.com

element = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/nav/ul/li[3]/a') # finds Enterprise button on github.com
element.click() # clicks on element (first way)
# element.send_keys(Keys.ENTER) # enters the element (which is commented - second way) 

sleep(5) # waits 5 seconds in Google.com
driver.quit() # closes the FireFox