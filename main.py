
import requests
from fastapi import FastAPI

app = FastAPI()


nombreDiccionarios = {
    'dolar':["turista",
    "qatar",
    "informal",
    "lujo",
    "contadoconliqui",
    "coldplay","mep",
    "mayorista",
    "oficial",
    "ahorro",
    "futuro",
    "nacion"]
    # "nombreDT":"turista",
    # "nombreDQ":"qatar",
    # "nombreDI":"informal",
    # "nombreDL":"lujo",
    # "nombreDCL":"contadoconliqui",
    # "nombreDCP":"coldplay",
    # "nombreDMP":"mep",
    # "nombreDMY":"mayorista",
    # "nombreDO":"oficial",
    # "nombreDA":"ahorro",
    # "nombreDF":"futuro",
    # "nombreDN":"nacion",
}

def rutaturista():
    url = 'https://mercados.ambito.com//dolarturista/variacion'
    json = requests.get(url).json()
    return json

def rutaqatar():
    url = 'https://mercados.ambito.com//dolarqatar/variacion'
    json = requests.get(url).json()
    return json

def rutainformal():
    url = 'https://mercados.ambito.com//dolar/informal/variacion'
    json = requests.get(url).json()
    return json

def rutalujo():
    url = 'https://mercados.ambito.com//dolardelujo/variacion'
    json = requests.get(url).json()
    return json

def rutacontadoconliqui():
    url = 'https://mercados.ambito.com//dolarrava/cl/variacion'
    json = requests.get(url).json()
    return json


def rutacoldplay():
    url = 'https://mercados.ambito.com//dolarcoldplay/variacion'
    json = requests.get(url).json()
    return json


def rutamep():
    url = 'https://mercados.ambito.com//dolarrava/mep/variacion'
    json = requests.get(url).json()
    return json


def rutamayorista():
    url = 'https://mercados.ambito.com//dolar/mayorista/variacion'
    json = requests.get(url).json()
    return json


def rutaoficial():
    url =  'https://mercados.ambito.com//dolar/oficial/variacion'
    json = requests.get(url).json()
    return json


def rutaahorro():
    url = 'https://mercados.ambito.com//dolarahorro/variacion'
    json = requests.get(url).json()
    return json


def rutafuturo():
    url = 'https://mercados.ambito.com//dolarfuturo/variacion'
    json = requests.get(url).json()
    return json


def rutanacion():
    url = 'https://mercados.ambito.com//dolarnacion//variacion'
    json = requests.get(url).json()
    return  json


def dolaruta(dolarname):
    if dolarname.lower() == "nacion":
        return rutanacion()
    elif dolarname.lower() == "futuro":
        return rutafuturo()
    elif dolarname.lower() == "ahorro":
        return rutaahorro()
    elif dolarname.lower() == "oficial":
        return rutaoficial()
    elif dolarname.lower() == "mayorista":
        return rutamayorista()
    elif dolarname.lower() == "mep":
        return rutamep()
    elif dolarname.lower() == "coldplay":
        return rutacoldplay()
    elif dolarname.lower() == "contadoconliqui":
        return rutacontadoconliqui()
    elif dolarname.lower() == "lujo":
        return rutalujo()
    elif dolarname.lower() == "informal":
        return rutainformal()
    elif dolarname.lower() == "qatar":  
        return rutaturista() 
    elif dolarname.lower() == "turista":  
        return rutaturista()      



#Robar datos semanales, mensuales y anuales de cada dolar
#Guardar datos historicos


@app.get('/data/{dolarname}')
def getdolardata(dolarname:str):
  dolardatos = dolaruta(dolarname=dolarname)
  return dolardatos
    

@app.get('/getdolars/')
def getdolarsendpoints():
    return nombreDiccionarios