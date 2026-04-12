import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=PYU5WSPQIGPOAKET
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_APIKEY = "PYU5WSPQIGPOAKET"

#https://newsapi.org/v2/everything?q=tesla&apiKey=42f8c248d8c6490aaff06fb66e9206c6
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = "42f8c248d8c6490aaff06fb66e9206c6"

TWILIO_SSD = "ACd3b2a9ead8a4b3f77c48418a8bbf8807"
TWILIO_AUTH = "4f3ed0d6a9c52ef80ad40d9b287f5e13"

weather_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_APIKEY
}

weather_response = requests.get(url=STOCK_ENDPOINT,params=weather_parameters)
weather_data = weather_response.json()["Time Series (Daily)"]
weather_data_list = [value for (key,value) in weather_data.items()]
today_closing_price = float(weather_data_list[0]["4. close"])
yesterday_closing_price = float(weather_data_list[1]["4. close"])
price_difference = today_closing_price - yesterday_closing_price
up_down_icon = ""

if price_difference > 0:
    up_down_icon = "🔺"
else:
    up_down_icon = "🔻"
    
price_difference_percentage = round((price_difference * 100) / today_closing_price,2)

if abs(price_difference_percentage) < 1:
    news_parameters = {
        "q": COMPANY_NAME,
        "apikey": NEWS_APIKEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    
    client = Client(TWILIO_SSD,TWILIO_AUTH)
    
    for article in three_articles:
        article_formatted = f"{STOCK}: {up_down_icon}{price_difference_percentage}%\nHeadline: {article["title"]}\nBrief:{article["description"]}"
        
        message = client.messages.create(
            body=article_formatted,
            from_= "+16085808112",
            to= "+18777804236"
        )
        print(message.body)