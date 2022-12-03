import requests

from url import url_dolares


def Getdolar(dolarname):
    for nombredolar, url in url_dolares.items():
        if f'dolar_{dolarname}'.lower() == nombredolar:
            dollar = requests.get(url).json()
            currency_data = {
                'name': nombredolar,
                'buy': dollar['compra'],
                'sell': dollar['venta'],
                'date': dollar['fecha'],
                'variation': dollar['variacion'],
                'class-variation': dollar['class-variacion'],
            }
    return currency_data

print(Getdolar('turista'))