# WRITE YOUR CODE HERE
import requests
import statsapi
import re

API_KEY = "79961ed861624e9291b6e4f42c2c83c0"

url = "https://api.sportsdata.io/v3/mlb/scores/json/ScoresBasic/2017-SEP-{}?key=79961ed861624e9291b6e4f42c2c83c0"

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY
}



#print(response.json())

for i in range(1, 31):
    print("2017 September " + str(i))
    day = str(i)
    if (len(day) < 2):
        day = "0" + day
    response = requests.get(url.format(day), headers=headers)
    allGames = response.json()
    numGames = len(allGames)
    for j in range(numGames):
         if (allGames[j]['AwayTeam'] == 'NYM' or allGames[j]['HomeTeam'] == 'NYM'):
             print(allGames[j])

        # regex to get NY teams
        # awayteam = allGames[j]['AwayTeam']
        # if(re.search("^N", awayteam)):
        #     print(awayteam)