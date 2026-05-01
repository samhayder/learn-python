from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price.text}.{price_fraction.text}")


driver.quit()
