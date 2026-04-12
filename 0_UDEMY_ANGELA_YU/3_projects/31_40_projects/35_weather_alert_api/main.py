import requests
from twilio.rest import Client

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast?"
WEATHER_APIKEY = "2fa8586e9de751499c09013180b8ce42"
MY_LAT = "23.707310"
MY_LON = "90.415482"
TWILIO_SSD = "ACd3b2a9ead8a4b3f77c48418a8bbf8807"
TWILIO_AUTH = "4f3ed0d6a9c52ef80ad40d9b287f5e13"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": WEATHER_APIKEY
}
rain_alert = False
alert_message = None

response = requests.get(url=WEATHER_ENDPOINT,params=parameters)
weather_data = response.json()

for i in weather_data["list"]:
    weather_condition = i["weather"][0]["id"]
    
    if weather_condition < 700:
        alert_message = f"Opps!: {i["weather"][0]["main"]} {i["weather"][0]["icon"]}\n{i["weather"][0]["description"]} (Bring Umbrella.)"
        rain_alert = True

if rain_alert:
    client = Client(TWILIO_SSD,TWILIO_AUTH)
    message = client.messages.create(
        body=alert_message,
        from_= "+16085808112",
        to= "+18777804236"
    )
    print(message.body)
