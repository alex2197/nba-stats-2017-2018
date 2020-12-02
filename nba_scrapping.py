import requests
import pandas as pd

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv";
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status() #Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")

nba = pd.read_csv("nba_all_elo.csv")
print(len(nba))
print(nba.head)