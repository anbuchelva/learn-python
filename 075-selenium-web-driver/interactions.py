from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_webdriver = Service("/snap/bin/chromium.chromedriver")
driver = webdriver.Chrome(service=chrome_webdriver)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count = driver.find_element_by_id("articlecount")
print(article_count.text)

# click using link text
all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.close()
# driver.quit()
