from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_webdriver = Service("/snap/bin/chromium.chromedriver")
driver = webdriver.Chrome(service=chrome_webdriver)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("my first name")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("my last name")

email = driver.find_element_by_name("email")
email.send_keys("me@email.com")

# email.send_keys(Keys.ENTER)
button = driver.find_element_by_css_selector("form button")
button.click()