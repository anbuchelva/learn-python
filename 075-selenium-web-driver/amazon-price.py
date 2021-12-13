from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service("/snap/bin/chromium.chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)
# driver = webdriver.Firefox()

driver.get(url="https://www.amazon.in/Intel-Performance-NUC11PAHI5-Thunderbolt-Pre-Installed/dp/B09BB9L9VR/")
try:
    price = driver.find_element_by_id("price_inside_buybox")
    print("using id")
except:
    price = driver.find_element_by_class_name("a-text-price")
    print("using class")

print(price.text)

driver.close()
driver.quit()
