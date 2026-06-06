URL = "https://appbrewery.github.io/fake-newsletter-signup/"

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("John")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Doe")

email = driver.find_element(By.NAME, "email")
email.send_keys("johndoe@example.com")

submit_button = driver.find_element(By.XPATH, '//*[@id="signup-form"]/button')
submit_button.click()