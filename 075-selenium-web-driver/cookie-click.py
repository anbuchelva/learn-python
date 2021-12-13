from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_webdriver = Service("/snap/bin/chromium.chromedriver")
driver = webdriver.Chrome(service=chrome_webdriver)
# driver = webdriver.Firefox()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")
expo = 5
timeout = time.time() + 5 * 60
interval = time.time() + expo
upgrade_price = []
upgrade_item = []
upgrade_attr = []


def get_price():
    price_list = driver.find_elements_by_css_selector("#store b")
    for item in price_list[:-1]:
        item_price = int(item.text.split(" - ")[1].split("\n")[0].replace(",", ""))
        upgrade_price.append(item_price)
    upgrade_price_sorted = upgrade_price[::-1]
    return upgrade_price_sorted


def get_item():
    price_list = driver.find_elements_by_css_selector("#store b")
    for item in price_list[:-1]:
        item_name = item.text.split(" - ")[0]
        upgrade_item.append(item_name)
    upgrade_item_sorted = upgrade_item[::-1]
    return upgrade_item_sorted


def get_attr():
    attr_list = driver.find_elements_by_css_selector("#store div")
    for item in attr_list[:-1]:
        attr_name = item.get_attribute("id")
        upgrade_attr.append(attr_name)
    upgrade_attr_sorted = upgrade_attr[::-1]
    return upgrade_attr_sorted


def power_up(price, attr):
    for n in range(len(price)):
        current_price = int(driver.find_element_by_id("money").text.replace(",", ""))
        if current_price > price[n]:
            return attr[n]


attr = get_attr()
item = get_item()
while time.time() < timeout:
    cookie.click()

    # check whether the powerup can happen for every interval
    if time.time() > interval:
        price = get_price()
        power_up_attr = power_up(price, attr)
        driver.find_element_by_id(power_up_attr).click()
        interval = time.time() + expo
        expo += 0.5

print(driver.find_element_by_id("cps").text)
driver.close()
