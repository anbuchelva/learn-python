from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service("/snap/bin/chromium.chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get(url="https://www.python.org/")

events = driver.find_element_by_class_name("event-widget")
events_list = events.text.splitlines()[2:]
driver.close()
driver.quit()

# Using for loop
# for i in range(0, len(events_list), 2):
#     events_dict[i] = {
#         "time": events_list[i],
#         "name": events_list[i+1],
#     }

# using comprehension
events_dict = {i: {"time": events_list[i], "name": events_list[i+1]} for i in range(0, len(events_list), 2)}
print(events_dict)
