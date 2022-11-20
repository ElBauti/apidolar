import requests
from url import *



def historicoone(dolarname, time):
    dato_dolar = {}
    for nombredolar, url in url_dolares.items():
        if f'dolar_{dolarname}'.lower() == nombredolar:
            dato_dolar[nombredolar] = requests.get(url).json()
            if time.lower() == "anual":
                    dato_dolar[nombredolar]["Dolar Historico Anual"] = requests.get(url_dolares_historico_anual[nombredolar]).json()
                    return dato_dolar
            elif time.lower() == "mensual":
                    dato_dolar[nombredolar]["Dolar Historico Mensual"] = requests.get(url_dolares_historico_mensual[nombredolar]).json()
                    return dato_dolar
            elif time.lower() == "semanal":
                    dato_dolar[nombredolar]["Dolar Historico Semanal"] = requests.get(url_dolares_historico_semanal[nombredolar]).json()
                    return dato_dolar