import requests
from bs4 import BeautifulSoup

# The following function will be then imported to the discord to enhance its functionality
def parse_price_dynamic(quote):
  print(quote)
  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
  stockSymbol = quote
  url = 'https://finance.yahoo.com/quote/'+ stockSymbol + '/key-statistics?p=' + stockSymbol
  page = requests.get(url, headers=headers, timeout=5)

  soup = BeautifulSoup(page.text, 'html.parser')

  price = soup.find_all('div', {'class':'D(ib) Mend(20px)'})[0].find('fin-streamer')['value']

  return "The price of " + quote + ": $" + str(price)