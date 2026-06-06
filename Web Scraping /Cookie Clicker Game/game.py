URL = "https://ozh.github.io/cookieclicker/"

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

language_selection = driver.find_element(By.ID, "langSelect-EN")
language_selection.click()

cookie = driver.find_element(By.ID, "bigCookie")
cookie.click()



