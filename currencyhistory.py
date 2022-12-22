import requests
from url import *
import dateparser

def createhistory(currency_data):
    dolar_historico = []
    for elm in range(1,len(currency_data)):
            fecha = dateparser.parse(currency_data[elm][0])
            precio = currency_data[elm][1]
            dolar = {
                     "date":fecha,
                     "value":precio
                 }
            dolar_historico.append(dolar)
    return dolar_historico