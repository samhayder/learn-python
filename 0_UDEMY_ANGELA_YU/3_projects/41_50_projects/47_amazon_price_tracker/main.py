import requests
from bs4 import BeautifulSoup
import smtplib
# env
import os
from dotenv import load_dotenv
load_dotenv()

#smtplib 
# my_mail = "sams.seul@gmail.com"
# password = "ugji mwpp xaig kacr"
# smtp_host = "smtp.gmail.com"

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    "Priority": "u=0, i",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-69f0df79-54b5a9226b9d145e5628712c"
}

response = requests.get(live_url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

product_name = soup.find(id="productTitle").getText()
product_price = soup.find(class_="a-offscreen").getText()
actual_product_price = float(product_price.split("$")[1])

product_message = f"{product_name}\n is now {product_price} \n {live_url}"

if actual_product_price < 80:
    with smtplib.SMTP(host=os.environ["smtp_host"]) as connection:
        connection.starttls()
        connection.login(user=os.environ["my_mail"],password=os.environ["password"])
        connection.sendmail(
            from_addr=os.environ["my_mail"],
            to_addrs=os.environ["my_mail"],
            msg=f"Subject:Amazon Price Alert\n\n{product_message.encode(encoding="ascii",errors="replace")}"
        )
        print(product_message)
else:
    print("Product is to high.")






