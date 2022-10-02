import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "AEUZM868O0UOSQWV"

NEWS_API_KEYS ="b113ad1d487f41a1984203ff6a964bfa"

TWILIO_SID = "AC5424ff2f1d5cc4c9f122c1d525eb831f"
TWILIO_AUTH_TOKEN = "94db29fb5ec1bf144e44bd9ad41ae93b"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response =  requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [values for (key, values) in data.items()]
yesterday_data = data_list[0]

yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

diffrence = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

diff_percent = (diffrence/float(yesterday_closing_price)) * 100

if diff_percent>5:
    print("Get news")

if diff_percent>1:
     news_params ={
        "apikey":NEWS_API_KEYS,
        "qInTitle":COMPANY_NAME
     }

     news_response = requests.get(NEWS_ENDPOINT, params=news_params)
     articles = news_response.json()["articles"]
     three_articles = articles[:3]
     form = [f"Headline:{article['title']}. \nBrief {article['description']}" for article in three_articles]
     client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

     for articless in form:

         message = client.messages.create(
              body=articless,
              from_="+15087948905",
              to="+919026734065",
         ) 