# WRITE YOUR CODE HERE
import requests
import statsapi

API_KEY = "79961ed861624e9291b6e4f42c2c83c0"

url = "https://api.sportsdata.io/v3/mlb/scores/json/ScoresBasic/2017-SEP-01?key=79961ed861624e9291b6e4f42c2c83c0"

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY
}

response = requests.get(url, headers=headers)

print(response.json())