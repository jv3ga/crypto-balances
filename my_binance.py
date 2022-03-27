from secretito import BINANCE_API as API_KEY, BINANCE_SECRET as API_SECRET
from calculate_prices import calular_precio_btc, calular_precio_usd
from binance import Client


def get_binance_data ():
    request_client = Client(api_key=API_KEY, api_secret=API_SECRET)
    data = request_client.get_account()
    return data

def get_binance_balance ():
    data = get_binance_data()
    return data['balances']

def get_binance_balance_formatted ():
    balance = get_binance_balance()
    balance['free'] = balance['cantidad']
    del balance['free']
    return balance

def print_binance_balance ():
    balance = get_binance_balance()
    for asset in balance:
        if float(asset['free']) != 0 or float(asset['locked']) != 0:
            moneda = asset['asset']
            cantidad  = float(asset['free'])
            total_usd = calular_precio_usd(moneda, cantidad)
            total_btc = calular_precio_btc(moneda, cantidad)
            print('Moneda:{}: - Cantidad: {} - Precio: {} BTC - {} USD'.format(
                moneda, cantidad, total_btc, total_usd
                )
            )

if __name__=="__main__":
    binance = print_binance_balance()