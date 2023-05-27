from bs4 import BeautifulSoup
import requests

class CurrencyConverter:
    def __init__(self):
        self.url = "https://www.oschadbank.ua/currency-rate"
        self.currency_data = {}

    def get_exchange_rates(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup_list = soup.find_all("span", class_="heading-block-currency-rate__table-txt body-regular")
            self.currency_data["USD"] = float(soup_list[9].text.replace(",", "."))

    def convert_to_usd(self, amount, currency):
        if currency not in self.currency_data:
            print("Invalid currency.")
            return None
        usd_amount = amount / self.currency_data[currency]
        return usd_amount

converter = CurrencyConverter()
converter.get_exchange_rates()

amount = float(input("Enter the amount in your local currency: "))
currency = input("Enter your currency code (e.g., USD, EUR): ")

usd_amount = converter.convert_to_usd(amount, currency)
if usd_amount is not None:
    print("Amount in USD:", usd_amount)
