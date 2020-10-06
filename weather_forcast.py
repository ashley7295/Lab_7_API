from pprint import pprint
import requests
import os

#program used to get the weater data for a city requested by the user, uses a temporary API key

url = f'http://api.openweathermap.org/data/2.5/weather'
key = os.environ.get('WEATHER_KEY')

def main(): #run functions in main and check for errors in the URL/Key
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Error: cannot get weather')
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp}F')

def get_location(): #get and check data from the user
    city, country = '',''
    while len(city) == 0:
        city = input('Please enter the city you would like the weather for: ')
    
    while len(country) != 2 or not country.isalpha:
        country = input('Please enter the 2 letter country code associated with that city: ')
        location = f'{city},{country}'

    return location

def get_current_weather(location, key): #takes user inputed location and global key to get the weather
    try:
        querie = {'q': location, 'units': 'imperial', 'appid': key}
        response = requests.get(url, params=querie)
        response.raise_for_status()
        data = response.json() #might also cause an error if response is not JSON
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text) #use logging here?
        return None, ex #tuple of data and exception

def get_temp(weather_data): #gets the specific data we want from the API and checks for errors
    try:
        temp = weather_data['main']['temp']
        return temp
    except KeyError:
        print('Error with data formating')
        return 'unknown'

if __name__ == '__main__':
    main()