import requests
from bs4 import BeautifulSoup


def gen_joke():
    # Make a request
    response = requests.get('http://www.laughfactory.com/jokes/latest-jokes')

    # Parse the content
    soup = BeautifulSoup(response.content, 'html.parser')

    joke_container = soup.find_all('div', {'class': 'joke-text'})[0]

    if joke_container:
        return joke_container.p.text
    else:
        return "No Jokes Found"
