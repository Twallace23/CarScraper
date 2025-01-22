#Selenium1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "/Users/tayvianwallace/Downloads/chromedriver-mac-arm64/chromedriver"

#So adding a service fixed the issue with our path being passed as a string
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.cars.com")
print(driver.title)


price_elements = driver.find_elements(By.CLASS_NAME, "primary-price")

filtered_prices = []
for element in price_elements:
    price_text = element.text.strip().replace(",","").replace("$","")
    if price_text.isdigit():
        price = float(price_text)
        if price < 10000:
            filtered_prices.append(price)

# Print filtered prices
print("Prices less than 10,000:", filtered_prices)


driver.quit()