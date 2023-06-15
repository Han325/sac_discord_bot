import requests
import json

def get_crypto_price():
    base_url = "https://api.coingecko.com/api/v3/coins/"
    response = requests.get(base_url + "bitcoin")
    crypto_data = json.loads(response.text)
    price = crypto_data['market_data']['current_price']['usd']
    return "Master, the price of " + "bitcoin" + " as of now is $" + str(price)

