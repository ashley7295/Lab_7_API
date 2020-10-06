from pprint import pprint
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=imperial&appid=36b75f061985cda7da1de6b1bfcbeedf'
data = requests.get(url).json()


temp = data['main']['temp']
print(f'The current temperature is {temp}F')