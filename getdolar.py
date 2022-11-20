import requests

from url import url_dolares


def Getdolar(dolarname):
    for nombredolar, url in url_dolares.items():
        if f'dolar_{dolarname}'.lower() == nombredolar:
            dato_dolar = {}
            dato_dolar[nombredolar] = requests.get(url).json()
    return dato_dolar