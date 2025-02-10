import okx.MarketData as MarketData

flag = "0"  # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag, debug=False)


def get_data_price(coins):
    result = marketDataAPI.get_ticker(instId=coins)
    return result['data'][0]


def default_price():
    result = get_data_price(coins='BTC-USDT')
    sodutc8_price = float(result['sodUtc8'])
    sodutc0_price = float(result['sodUtc0'])
    last = float(result['last'])
    procent = (last - sodutc0_price) / sodutc0_price * 100

    item_data = {
        'last': last,
        'interests': procent
    }
    if item_data['interests'] < 0:
        return f"{last}$ 🟥 ⬇️"
    else:
        return f"{last}$ 🟩 ⬆️"


def custom_price(coins):
    data = get_data_price(coins)
    sodutc0_price = float(data['sodUtc0'])
    last = float(data['last'])
    procent = (last - sodutc0_price) / sodutc0_price * 100

    item_data = {
        'last': last,
        'interests': procent
    }
    if item_data['interests'] < 0:
        return f"{last}$ 🟥 ⬇️"
    else:
        return f"{last}$ 🟩 ⬆️"