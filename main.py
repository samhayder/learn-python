import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.facebook.com/")
soup = BeautifulSoup(url.content, "html.parser")

print(soup.prettify())