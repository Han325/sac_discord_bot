import requests
import bs4
from bs4 import BeautifulSoup


def parse_price():
  request = requests.get("https://finance.yahoo.com/quote/TSLA")
  soup = bs4.BeautifulSoup(request.text, "html.parser")

  print(soup)


parse_price()