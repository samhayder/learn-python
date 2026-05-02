from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url="https://appbrewery.github.io/gym/")

#Register & Log in automatically
NAME = "samsuddin"
EMAIL = "same.seul@gmail.com"
PASSWORD = "se0181133"

book_counter = 0
already_book_counter = 0
waitlist_counter = 0

sleep(2)
login_btn = driver.find_element(By.ID, value="login-button")
login_btn.click()
sleep(1)
# Resister
resister_btn = driver.find_element(By.ID, value="toggle-login-register")
resister_btn.click()
resister_name = driver.find_element(By.XPATH, value='//*[@id="name-input"]')
resister_email = driver.find_element(By.XPATH, value='//*[@id="email-input"]')
resister_password = driver.find_element(By.XPATH, value='//*[@id="password-input"]')
signup_btn = driver.find_element(By.XPATH, value='//*[@id="submit-button"]')

resister_name.clear()
resister_email.clear()
resister_password.clear()

resister_name.send_keys(NAME)
resister_email.send_keys(EMAIL)
resister_password.send_keys(PASSWORD)

signup_btn.click()

sleep(1)

#Book specific gym classes (book-button-spin-2026-05-05-0800)
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            # Check if already booked
            if button.text == "Booked":
                already_book_counter += 1
                print(f"✓ Already booked: {class_name} on {day_title}")
            elif button.text == "Waitlisted":
                already_book_counter += 1
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
            elif button.text == "Book Class":
                # Book the class
                button.click()
                book_counter += 1
                print(f"✓ Successfully booked: {class_name} on {day_title}")
            elif button.text == "Join Waitlist":
                # Join waitlist if class is full
                button.click()
                waitlist_counter += 1
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
            break
sleep(2)

# print Summery
print("--- BOOKING SUMMARY ---")
print(f"Classes booked: {book_counter}")
print(f"Waitlists joined: {waitlist_counter}")
print(f"Already booked/waitlisted: {already_book_counter}")
print(f"Total Tuesday 6pm classes processed: {book_counter + waitlist_counter + already_book_counter}")