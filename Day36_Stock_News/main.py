import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "62SNXQ2NZGQ6ZSJ1"
NEWS_API = "9191944549814e52af356a14e94c1067"

account_sid = os.environ.get("ACCOUNT_ID")
auth_token = os.environ.get("AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "interval": "1min",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}

news_params = {
    "qInTitle": "Tesla",
    "apiKey": NEWS_API,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (1min)"]
stock_price_list = [value for (key, value) in data.items()]
stock_price_yesterday = float(stock_price_list[0]['4. close'])

stock_price_day_bef_yesterday = float(stock_price_list[1]['4. close'])
print(stock_price_yesterday)
print(stock_price_day_bef_yesterday)

difference = (stock_price_yesterday - stock_price_day_bef_yesterday)
abs_difference = abs(difference)
print(abs_difference)

percentage_diff = round(abs_difference / stock_price_yesterday * 100, 2)
print(percentage_diff)


def get_news():
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][0:3]
    news_title_list = [item["title"] for item in news_data]
    return news_title_list


if percentage_diff > 0:
    headlines = get_news()
    for headline in headlines:
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=f"{headline}", from_="phone", to="phone")
