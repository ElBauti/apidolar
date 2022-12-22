import requests
from url import *
from currencyhistory import *

def Historicoall(dolarname):
    for nombredolar, url in url_dolares.items():
        if f'dolar_{dolarname}'.lower() == nombredolar:
    #             'Historico_Mensual': createhistory(requests.get(url_dolares_historico_mensual[nombredolar]).json()),
    #             'Historico_Semanal': createhistory(requests.get(url_dolares_historico_semanal[nombredolar]).json())
            Historico_Anual =  createhistory(requests.get(url_dolares_historico_anual[nombredolar]).json())
    return Historico_Anual
