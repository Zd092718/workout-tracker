import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "158.7"
HEIGHT_CM = "190"
AGE = "27"

APP_ID = "fb52b1ea"
API_KEY = "c773a2db2f66a342200239592349ccbd"

stats_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_post_endpoint = "https://api.sheety.co/244048922277da09ec695fdc582fdadc/myWorkouts/workouts"

exercise_query = input("Tell me which exercises you did: ")

stats_params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

stats_response = requests.post(url=stats_endpoint, json=stats_params, headers=headers)
data = stats_response.json()
print(data)




sheets_post_response = requests.post(url=sheets_post_endpoint)