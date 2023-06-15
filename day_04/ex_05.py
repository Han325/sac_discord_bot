import requests
import random


def get_random_global_news(keywords):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": "3c6086135867405f9ce6113509f729c5",
        "q": keywords,
    }
    response = requests.get(url, params=params)
    news = response.json()

    article = random.choice(news["articles"])

    return article["url"]

