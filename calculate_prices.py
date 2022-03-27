import requests

# ToDo: utilizar otra api para buscar precios, no están todos las moneadas

def calular_precio_btc(asset, cantidad):
    url = 'https://data.messari.io/api/v1/assets/{}/metrics'.format(asset)
    data = requests.request('GET', url)
    if data.ok:
        price_btc = data.json()['data']['market_data']['price_btc']
        return cantidad * price_btc
    else:
        print('No se encuentra el activo {}'.format(asset))


def calular_precio_usd(asset, cantidad):
    url = 'https://data.messari.io/api/v1/assets/{}/metrics'.format(asset)
    data = requests.request('GET', url)
    if data.ok:
        price_usd = data.json()['data']['market_data']['price_usd']
        return cantidad * price_usd
    else:
        print('No se encuentra el activo {}'.format(asset))