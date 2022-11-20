import requests

from url import *

dolares_json = []
def Getdolares():
    for nombredolar, url in url_dolares.items():
        dato_dolar = {}
        dato_dolar[nombredolar] = requests.get(url).json()
        dolares_json.append(dato_dolar)
    return dolares_json