from fastapi import FastAPI

from calculadora import calculadoradolar
from getdolar import Getdolar
from getdolars import Getdolares
from historico import historicoone
from url import *

app = FastAPI()

#Guardar datos historicos


@app.get('/getdolar/{dolarname}')
def getdolar(dolarname:str):
    return Getdolar(dolarname)

    
@app.get('/getdolars/')
def dolares():
    return Getdolares()

@app.get('/calculadora/{compraoventa}/{dolarname}/{dolarunid}')
def calculates(dolarname, dolarunid, compraoventa):
    return calculadoradolar(dolarname, dolarunid, compraoventa)

@app.get('/historico/{dolarname}/{time}')
def historicos(dolarname,time):
    return historicoone(dolarname=dolarname,time=time)