import csv
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movie_titles.reverse()

with open("movie_titles.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Movie Title"])
    for title in movie_titles:
        writer.writerow([title])

print(f"Saved {len(movie_titles)} movie titles to movie_titles.csv")


