URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

number_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[1]/a')
# print(number_of_articles.text)
# number_of_articles.click()

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python (programming language)")
search_box.submit()