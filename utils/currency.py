import requests 


def get_currency(url="https://api.monobank.ua/bank/currency") -> dict:
    response = requests.get(url)
    data = response.json()
    usd_buy = data[0]["rateBuy"]
    usd_sell = data[0]["rateSell"]
    eur_buy = data[1]["rateBuy"]
    eur_sell = data[1]["rateSell"]

    currency_data = {
        'usdbuy': usd_buy,
        'usdsell': usd_sell,
        'eurbuy': eur_buy,
        'eursell': eur_sell
    }
    return currency_data

