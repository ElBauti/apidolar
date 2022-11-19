from fastapi import FastAPI

from Calculadora import calculate
from Historico import historico
from Rutas import *
from Urls import *

app = FastAPI()

#Guardar datos historicos


@app.get('/data/{dolarname}')
def getdolardata(dolarname:str):
    dolardatos = dolaruta(dolarname=dolarname)
    return dolardatos
    
@app.get('/getdolars/')
def dolares():
    return dolars()

@app.get('/calculadora/{compraoventa}/{dolarname}/{dolarunid}')
def calculates(compraoventa, dolarname, dolarunid):
    resultadocalculo = calculate(dolarname, dolarunid, compraoventa)
    return resultadocalculo

@app.get('/historico/{dolarname}/{time}')
def historicos(dolarname,time):
    return historico(dolarname=dolarname,time=time)