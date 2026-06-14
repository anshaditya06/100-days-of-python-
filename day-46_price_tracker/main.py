URL = "https://www.amazon.in/Amazon-Brand-High-Speed-Rechargeable-Headlights/dp/B0DQG6CCY2/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.bbe41650-8528-49f7-9cc4-609b686366a2&dib=eyJ2IjoiMSJ9.vCNegsd4liGCjALZ2sQDhH1H-81Fd8FKiQC5E28jA8vzsBMnxQXGqksiIbI1gNiuIn9LY4sCiBVFjE4PtES1o7N7olk95VSUBkM_oaV0VVY.E3BnRVEKRIEBCkHHpGRLSamj_I8adwiRp2Q_Cs3SNFo&dib_tag=se&pd_rd_r=eb8e6a8f-9ca1-47e7-bc79-1cfbeb36f2a7&pd_rd_w=hnpUd&pd_rd_wg=1rc3v&qid=1780504359&sr=8-2&th=1"

from selenium import webdriver
from selenium.webdriver.common.by import By


# Create a ChromeOptions instance (not a WebDriver) to set options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_by_xpath = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]').text

print(price)
print(price_by_xpath)


driver.quit()