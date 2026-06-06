date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"


import requests
from bs4 import BeautifulSoup

response = requests.get(URL)
if response.status_code != 200:
    print(f"Failed to retrieve data for {date}. HTTP status code: {response.status_code}")
    print("The page may not exist for that date or the URL format has changed.")
    raise SystemExit

soup = BeautifulSoup(response.text, "html.parser")

song_names = soup.find_all(name="h3", class_="chart-entry__title")
song_artists = soup.find_all(name="span", class_="chart-entry__artist")

count = min(10, len(song_names), len(song_artists))
if count == 0:
    print("No songs found. The page structure may have changed or the date is invalid.")
    raise SystemExit

for i in range(count):
    print(song_names[i].getText().strip())

for i in range(count):
    print(song_artists[i].getText().strip())

