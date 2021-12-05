from bs4 import BeautifulSoup
import lxml
import requests
from requests.models import Response

with open("website.html") as file:
    contents = file.read()

# response = requests.get("https://anbuchelva.in")
# contents = response.text
soup = BeautifulSoup(contents, 'lxml')

# Print the entire html code
# print(soup)

# Print the entire html code with proper indentation
# print(soup.prettify)

# Print the Title of the page including <title> tag
# print(soup.title)

# Print the title without the tags
# print(soup.title.string)

# Print the first p tag from the website
# print(soup.p)

# Print all anchor tags from the page
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText()) # Prints the text
#     print(tag.get("href")) # Prints the href link

# Print all paragraph tags from the page
# all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)

# Find a tag with id = name
# heading = soup.find(name="h1", id="name")
# print(heading.string)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))


# with open("test.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'lxml')
# form_tag = soup.find("input")
# max_length = form_tag.get("maxlength")
# print(max_length)

# response = requests.get("https://www.facebook.com/tamilnaduweatherman")
# contents = response.text
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup)