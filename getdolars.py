import requests

from url import *

dolares_json = []
def Getdolares():
    for nombredolar, url in url_dolares.items():
        dollar = requests.get(url).json()
        currency_data = {
            'name': nombredolar,
            'buy': dollar['compra'],
            'sell': dollar['venta'],
            'date': dollar['fecha'],
            'variation': dollar['variacion'],
            'class-variation': dollar['class-variacion'],
        }
        dolares_json.append(currency_data)
    return dolares_json


# "compra": "167,89",
# "venta": "168,09",
# "fecha": "02/12/2022 - 16:06",
# "variacion": "0,22%",
# "class-variacion": "up"
