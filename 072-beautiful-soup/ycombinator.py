import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'lxml')

article_texts = []
article_links = []
article_upvotes = []

all_title = soup.findAll(name='a', class_="titlelink")
for title in all_title:
    article_texts.append(title.text)
    article_links.append(title.get('href'))

subtexts = soup.findAll(name="td", class_="subtext")
for subtext in subtexts:
    try:
        article_upvote = int(subtext.find(name="span", class_="score").getText().split(" ")[0])
    except AttributeError:
        article_upvote = 0
    article_upvotes.append(article_upvote)

max_score = max(article_upvotes)
max_sore_position = article_upvotes.index(max_score)
print(article_links[max_sore_position])
print(article_texts[max_sore_position])
print(article_upvotes[max_sore_position])
