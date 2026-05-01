from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')

# print(article.text)

#Find the search input by name tag
search = driver.find_element(By.NAME, value="search")

# send keys
search.send_keys("Python", Keys.ENTER)

# driver.quit()