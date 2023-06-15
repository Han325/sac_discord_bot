import requests
import random

def get_random_malaysia_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'country': 'my',  
        'apiKey': '3c6086135867405f9ce6113509f729c5', 
    }

    response = requests.get(url, params=params)
    news = response.json()

    article = random.choice(news['articles'])

    return article['url']
