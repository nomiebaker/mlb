# WRITE YOUR CODE HERE
import requests
import re
import sqlalchemy as db
import pandas as pd

API_KEY = "79961ed861624e9291b6e4f42c2c83c0"

url = "https://api.sportsdata.io/v3/mlb/scores/json/ScoresBasic/2017-SEP-{}?key=79961ed861624e9291b6e4f42c2c83c0"
#https://sportsdata.io/developers/api-documentation/mlb#/endpoint/scores-by-date

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY
}

def day3():
    response = requests.get(url.format('05'), headers=headers)
    mlb = pd.DataFrame.from_dict(response.json())
    engine = db.create_engine('sqlite:///mlb.db')
    mlb.to_sql('trymlb', con=engine, if_exists='replace', index=False)

    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT AwayTeam , HomeTeam FROM trymlb;")).fetchall()
        print(pd.DataFrame(query_result))

#print(response.json())
def day2() :
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

day3()