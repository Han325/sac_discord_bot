import requests
import json

def get_crypto_price_dynamic(crypto_name):
    base_url = "https://api.coingecko.com/api/v3/coins/"
    response = requests.get(base_url + crypto_name)
    crypto_data = json.loads(response.text)
    price = crypto_data['market_data']['current_price']['usd']
    return "Master, the price of " + crypto_name + " as of now is $" + str(price)

