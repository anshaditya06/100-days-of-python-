from bs4 import BeautifulSoup


with open("bs_start/website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)

heading = soup.find(name="h1", id="name")
print(heading.text)

company_url = soup.select_one(selector="p a")
print(company_url)