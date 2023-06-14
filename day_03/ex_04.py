import requests
from bs4 import BeautifulSoup
import geocoder

def get_weather():
    # Fetch location
    g = geocoder.ip('me')
    lat, long = g.latlng

    # Get weather data
    weather_url = f"https://weather.com/weather/today/l/{lat},{long}?par=google&temp=c"
    response = requests.get(weather_url)

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find temperature
    temp = soup.find('div', attrs={'CurrentConditions--primary--2DOqs'}).find('span').text
   
    return "The temperature in your area is: " + temp + "C"

