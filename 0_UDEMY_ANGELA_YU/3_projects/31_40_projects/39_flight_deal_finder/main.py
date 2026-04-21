import requests

# Sheety API
SHEETY_ENDPOINT = "https://api.sheety.co/d421d9f287f9ebb46a6ae3f99eae4441/flightPrice/sheet1"

sheety_header = {
    "Authorization": "Bearer 1PXI0o7MtRx8KB_8Jro433OiwX8Rgw-F322q5WA5fjE8"
}

sheety_response = requests.get(url=SHEETY_ENDPOINT,headers=sheety_header)
sheety_data = sheety_response.json()
print(sheety_data["sheet1"])