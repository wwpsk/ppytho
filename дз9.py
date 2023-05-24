import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.url = 'https://www.oschadbank.ua/'
        self.currency_class = 'currency-cash__rate'

    def get_exchange_rate(self, currency):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        currencies = soup.find_all(class_=self.currency_class)

        for currency_info in currencies:
            if currency in currency_info.text:
                exchange_rate = currency_info.find_next(class_=self.currency_class).text
                return float(exchange_rate.replace(',', '.'))

        return None

    def convert_to_usd(self, currency, amount):
        exchange_rate = self.get_exchange_rate(currency)

        if exchange_rate is not None:
            usd_amount = amount / exchange_rate
            return usd_amount

        return None


converter = CurrencyConverter()
currency = input('Введіть назву валюти своєї країни: ')
amount = float(input('Введіть суму валюти: '))

usd_amount = converter.convert_to_usd(currency, amount)
if usd_amount is not None:
    print(f'{amount} {currency} = {usd_amount:.2f} USD')
else:
    print('Не вдалося отримати курс обміну.')