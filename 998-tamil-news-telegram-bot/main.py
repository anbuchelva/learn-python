#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time

WORKING_DIRECTORY = "enter the path here"
TELEGRAM_BOT_TOKEN = "hidden"
TELEGRAM_CHAT_ID = "@tamil_news_alerts"


def alert(news_url):
    token = TELEGRAM_BOT_TOKEN
    parameters = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": news_url,
        "parse_mode": "Markdown"
    }
    response = requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?",
                            params=parameters)
    response.raise_for_status()


def get_html_links(url, find_method):
    links = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)

    if find_method == 'Dinamalar':
        dinamalar_ur_ls = []
        all_anchor_tags = soup.find_all(name="a")
        for tag in all_anchor_tags:
            dinamalar_ur_ls.append(str(tag.get("href")))
        for link in dinamalar_ur_ls:
            if link[0:19] == "news_detail.asp?id=" and link[-7:] != "comment" and link[-8:] != "comments":
                links.append(f"https://www.dinamalar.com/{link}")

    elif find_method == 'News18':
        news18_urls = []
        all_anchor_tags = soup.find_all(name="a")
        for tag in all_anchor_tags:
            news18_urls.append(str(tag.get("href")))
            # print(links)
        for link in news18_urls:
            if link[-4:] == "html":
                if link[0:1] == "/":
                    links.append(f"https://tamil.news18.com{link}")
                else:
                    links.append(link)

    else:
        for link in soup.find_all('a', find_method):
            links.append(link['href'])

    unique_url_list = list(set(links))
    # print(unique_url_list)
    return unique_url_list


newspapers = [
    {
        "name": "Dinamani",
        "url": "https://www.dinamani.com/latest-news",
        "find_method": {"class": "article_click"},

    },
    {
        "name": "Vikatan",
        "url": "https://www.vikatan.com/latest-news",
        "find_method": {"class": "undefined"},
    },
    {
        "name": "Vikatan",
        "url": "https://www.vikatan.com/news/tamilnadu",
        "find_method": {"class": "undefined"},
    },
    {
        "name": "Vikatan",
        "url": "https://www.vikatan.com/news/world",
        "find_method": {"class": "undefined"},
    },
    {
        "name": "Dinamani",
        "url": "https://www.dinamani.com/",
        "find_method": {"class": "article_click"},
    },
    {
        "name": "Puthiya-Thalaimurai",
        "url": "https://www.puthiyathalaimurai.com/news/justin",
        "find_method": {"class": "linear_text"},
    },
    {
        "name": "Dinamalar",
        "url": "https://www.dinamalar.com/",
        "find_method": "Dinamalar",
    },
    {
        "name": "News18Tamil",
        "url": "https://tamil.news18.com/",
        "find_method": "News18",
    },
]

for newspaper in newspapers:

    url_list = get_html_links(url=newspaper["url"], find_method=newspaper["find_method"])

    news = open(f"{WORKING_DIRECTORY}/news.csv", "w")
    for element in url_list:
        news.write(element + "\n")
    news.close()

    with open(f"{WORKING_DIRECTORY}/olds.csv") as f:
        olds = f.read().splitlines()

    latest_news = []
    for line in url_list:
        if line not in olds:
            latest_news += [line]
            # print(f"{line} #{newspaper['name']}")
    #        alert(line)

    # latest_news.sort()
    olds_file = open(f"{WORKING_DIRECTORY}/olds.csv", "a")
    for line in latest_news:
        alert(f"{line} #{newspaper['name']}")
        olds_file.write(line + "\n")
        time.sleep(4)
    olds_file.close()
