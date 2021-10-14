import requests
from datetime import date, timedelta

# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
stock_api_endpoint = "https://www.alphavantage.co/query"
stock_api_params = {
    "function": "CRYPTO_INTRADAY",
    "symbol": "BTC",
    "market": "USD",
    "interval": "60min",
    "apikey": "<hidden>"
}
stock_response = requests.get(stock_api_endpoint, params=stock_api_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series Crypto (60min)"]
# print(stock_data)
first_item = stock_data[list(stock_data)[0]]
fourth_item = stock_data[list(stock_data)[3]]
twenty_fourth_item = stock_data[list(stock_data)[23]]
close_value = float(fourth_item["4. close"])
close_24_value = float(twenty_fourth_item["4. close"])
open_value = float(first_item["1. open"])
change_percent = round((close_value - open_value) / close_value * 100, 3)
change_percent_24hours = round((close_24_value - open_value) / close_24_value * 100, 3)
# print(change_percent)
# print(close_value, open_value)
# print(first_item)


today = date.today()
yesterday = date.today() - timedelta(days=1)

news_api_endpoint = "https://newsapi.org/v2/everything"
news_api_params = {
    "qInTitle": "bitcoin",
    "apiKey": "<hidden>",
    "from": "yesterday",
    "to": "today",
    "sortBy": "publishedAt",
    "pageSize": 3,
    "language": "en"
}

news_response = requests.get(news_api_endpoint, params=news_api_params)
news_response.raise_for_status()
# print(news_response.json()["articles"])
news_data = news_response.json()["articles"]
news1_title = news_data[0]['title']
news1_context = news_data[0]['description']
news1_url = news_data[0]['url']
news2_title = news_data[1]['title']
news2_context = news_data[1]['description']
news2_url = news_data[1]['url']
news3_title = news_data[2]['title']
news3_context = news_data[2]['description']
news3_url = news_data[2]['url']
news1 = f"Title: {news1_title} \nNews: {news1_context} \nMore Info: {news1_url}"
news2 = f"Title: {news2_title} \nNews: {news2_context} \nMore Info: {news2_url}"
news3 = f"Title: {news3_title} \nNews: {news3_context} \nMore Info: {news3_url}"

if change_percent > 0:
    stock_details = f"Bitcoin 4 hours interval: 🔺{change_percent}% \n" \
                    f"Close: {close_value} | Open: {open_value} | Diff: {round(close_value - open_value,2)}\n"
else:
    stock_details = f"Bitcoin 4 hours interval: 🔻{change_percent}% \n" \
                    f"Close: {close_value} | Open: {open_value} | Diff: {round(close_value - open_value,2)}\n"

if change_percent_24hours > 0:
    stock_details += f"Bitcoin 24 hours interval: 🔺{change_percent_24hours}% \n" \
                     f"Close: {close_24_value} | Open: {open_value} | Diff: {round(close_24_value - open_value,2)}\n"
else:
    stock_details += f"Bitcoin 24 hours interval: 🔻{change_percent_24hours}% \n" \
                     f"Close: {close_24_value} | Open: {open_value} | Diff: {round(close_24_value - open_value,2)}\n"


token = "<hidden>"
parameters = {
    "chat_id": "@KP9IOeCvyu2Rs2kl",
    "text": f"{stock_details}\n{news1}\n\n{news2}\n\n{news3}",
    "parse_mode": "Markdown"
}
response = requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?",
                        params=parameters)
response.raise_for_status()
