from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

tag_list = ['python']

username = open(r'C:\Users\AliAghaNajm\Desktop\selenium_project\username.txt', 'r').readline()
password = open(r'C:\Users\AliAghaNajm\Desktop\selenium_project\password.txt', 'r').readline()

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')

driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password + Keys.ENTER)
sleep(5)

url_list = []
for tag in tag_list:
    driver.get('https://www.instagram.com/explore/tags/' + tag)
    sleep(5)
    
    for scroll in range(0, 3):
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        sleep(2)

    sleep(5)
    post_list = driver.find_elements(By.CSS_SELECTOR, '._aanf > a')
    for post in post_list:
        url_list.append(post.get_attribute('href'))

    for url in url_list:
        driver.get(url)
        sleep(5)   
        x_path = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div' 
        f_btn  = driver.find_element(By.XPATH, x_path)
        if f_btn.text == 'Follow':
            f_btn.click()
        l_btn = driver.find_element(By.CSS_SELECTOR, '._aamw > button').click()
        sleep(5)

        comment_box = driver.find_element(By.CSS_SELECTOR, '[class="_ablz _aaoc"]')
        # print(comment_box)
        comment_box.send_keys('Wooow dude!!!!' + Keys.ENTER)
        # webdriver.ActionChains(driver).click().send_keys('Wooow dude, I am Robot' + Keys.ENTER).perform()
        sleep(5)
        
        
sleep(20)
driver.quit()