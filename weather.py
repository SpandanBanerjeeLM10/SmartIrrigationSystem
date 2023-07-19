import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "f11f1cca7c1b286b80f05a84138b03a6"
CITY = "DUBLIN"

def tempConverter(kelvin):
    cel = kelvin - 273.5
    return cel

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()



temp_kelvin = response['main']['temp']
temp_cel = tempConverter(temp_kelvin)

humidity = response['main']['humidity']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Temperature in {CITY}: {temp_cel:.2f} deg Cel")
print(f"Humidity in {CITY}: {humidity}%")
