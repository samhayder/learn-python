from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url="https://www.python.org/")

event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_times = [event.text for event in driver.find_elements(By.CSS_SELECTOR, value=".event-widget li time")]
event_names = [event.text for event in driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")]

events = {}

for n in range(len(event_times)):
    events[n] = {
        "Time": event_times[n],
        "Name": event_names[n]
    }

print(events)


driver.quit()