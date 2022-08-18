from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox() # opens FireFox
driver.get('https://google.com') # Goes to Google.com
s_box = driver.find_element(By.NAME, 'q') # finds search box in Google.com

text = 'SELENIUM IS AN IMPORTANT LIBRARY IN PYTHON'
text = text.lower() # decapitalize all the text 

count = 0
for letter in text:
    if count % 2 == 0:
        webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys(letter).key_up(Keys.SHIFT).perform()
    else:
        s_box.send_keys(letter)
    sleep(0.25)    
    count += 1    

s_box.send_keys(Keys.ENTER)    
sleep(5) # waits 5 seconds in Google.com
driver.quit() # closes the FireFox