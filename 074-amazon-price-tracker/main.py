import requests
from bs4 import BeautifulSoup
from telegram import send_message

PRODUCT_URL = "https://www.amazon.in/Intel-Performance-NUC11PAHI5-Thunderbolt-Pre-Installed/dp/B09BB9L9VR/"
HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Accept-Language": "en-US,en;q=0.5",
}

expected_price = 25000

response = requests.get(url=PRODUCT_URL, headers=HEADER)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(id="priceblock_ourprice").getText()

price_without_currency = price.split("₹")[1].replace(",", "")
price_in_float = float(price_without_currency)

product_name = soup.find(id="productTitle").getText().strip()
# print(product_name)

message = f"The price of **{product_name}** has dropped below ₹{expected_price} and now it is at ₹{price_in_float}." \
          f"\n\ncheck out from here: {PRODUCT_URL}"

if price_in_float < expected_price:
    send_message(message)
