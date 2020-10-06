import requests
from pprint import pprint




url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url)
data = response.json()

#pprint(data)

dollars_exchange_rate = data['bpi']['USD']['rate_float']

print(dollars_exchange_rate)


bitcoin_amount = float(input('How many bitcoins do you have?: '))

bitcoin_value = bitcoin_amount * dollars_exchange_rate

print(f'{bitcoin_amount} Bitcoin is equivilent to ${bitcoin_value}')