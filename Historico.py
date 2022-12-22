import requests
from url import *
from currencyhistory import *

def Historicoone(dolarname, time):
    dato_dolar = {}
    for nombredolar, url in url_dolares.items():
        if f'dolar_{dolarname}'.lower() == nombredolar:
            dato_dolar[nombredolar] = requests.get(url).json()
            if time.lower() == "anual":
                return createhistory(requests.get(url_dolares_historico_anual[nombredolar]).json())
            elif time.lower() == "mensual":
                return createhistory(requests.get(url_dolares_historico_mensual[nombredolar]).json())
            elif time.lower() == "semanal":
                return createhistory(requests.get(url_dolares_historico_semanal[nombredolar]).json())

