import requests
# date format RRRR-MM-DD
def get_today_currency_rate(currency, date):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}"
    r = requests.get(url)
    my_json = r.json()
    return my_json.get('rates')[0].get('mid')


date = '2021-05-20'
today_currencies_rates = {
                            'EUR': get_today_currency_rate('EUR', date),
                            'GBP': get_today_currency_rate('GBP', date),
                            'USD': get_today_currency_rate('USD', date),
                            'CHF': get_today_currency_rate('CHF', date)
                          }
#print(today_currencies_rates)

#print(get_today_currency_rate('CHF', date))
