import requests
from datetime import datetime

#Nutrition api_id & api_key
API_KEY = "nix_live_kqF04FajtapMtddXU7C4xrmWY4UF49VQ"
APP_ID = "app_5403bd84f3fe41af8b74fdd7"

nutrition_api_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_api_endpoint = "https://api.sheety.co/d421d9f287f9ebb46a6ae3f99eae4441/workoutTracking/workouts"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutrition_parameter = {
    "query": input("Tell me which exercise you did? ")
}

response = requests.post(url=nutrition_api_endpoint,json=nutrition_parameter,headers=headers)
result = response.json()

# print(result['exercises'][0])

sheety_header = {
    "Authorization": "Bearer 016ridoy0048438"
}

today = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%x")

for exercise in result["exercises"]:
    # print(exercise['user_input'])
    sheet_input = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheet_response = requests.post(url=sheety_api_endpoint,json=sheet_input,headers=sheety_header)
    print(sheet_response.text)
    
