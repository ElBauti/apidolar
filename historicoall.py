import requests
from url import *

def Historicoall(dolarname):
    dato_dolar = {}
    for nombredolar, url in url_dolares.items():
        if f'dolar_{dolarname}'.lower() == nombredolar:
            dato_dolar[nombredolar] = requests.get(url).json()
            dato_dolar[nombredolar]["Dolar_Historico_Anual"] = requests.get(url_dolares_historico_anual[nombredolar]).json()
            dato_dolar[nombredolar]["Dolar_Historico_Mensual"] = requests.get(url_dolares_historico_mensual[nombredolar]).json()
            dato_dolar[nombredolar]["Dolar_Historico_Semanal"] = requests.get(url_dolares_historico_semanal[nombredolar]).json()
            return dato_dolar