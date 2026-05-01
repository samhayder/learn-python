from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sing_up = driver.find_element(By.CSS_SELECTOR, value=".btn-block")

f_name.send_keys("Samsuddin")
l_name.send_keys("Hayder")
email.send_keys("sams.seul@gmail.com")
sing_up.click()