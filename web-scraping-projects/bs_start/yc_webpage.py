import requests
from bs4 import BeautifulSoup
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])