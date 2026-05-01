from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import time,sleep

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url="https://ozh.github.io/cookieclicker//")

sleep(3)
try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    # print("Found language button, clicking...")
    language_button.click()
    sleep(3)
except NoSuchElementException:
    print("Not Found Language button...")
    
sleep(2)

cookie = driver.find_element(by=By.ID, value="bigCookie")

timeout = time() + (0.1*60)

while True:
    cookie.click()
    
    if time() > timeout:
        try:
            cookie_count = driver.find_element(By.CSS_SELECTOR, value="#cookies")
            print(f"Total number of cookie: {cookie_count.text}")
        except NoSuchElementException:
            print("Could'n get final cookie count.")
        break
        
