import requests
import json

def get_match():
    r = requests.get("https://api.opendota.com/api/matches/7400987864")
    data = r.json()
    return data

print(len(get_match()))