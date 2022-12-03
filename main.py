from fastapi import FastAPI

from calculadora import Calculadoradolar
from getdolar import Getdolar
from getdolars import Getdolares
from historico import Historicoone
from historicoall import Historicoall
from url import *

app = FastAPI()

@app.get('/getDollar/{dolarname}')
def getdolar(dolarname:str):
    return Getdolar(dolarname)

@app.get('/getDollars/')
def dolares():
    return Getdolares()

@app.get('/calculadora/{compraoventa}/{dolarname}/{dolarunid}')
def calculates(dolarname, dolarunid, compraoventa):
    return Calculadoradolar(dolarname, dolarunid, compraoventa)

@app.get('/historicoOne/{dolarname}/{time}')
def historicos(dolarname,time):
    return Historicoone(dolarname=dolarname,time=time)

@app.get('/historicAll/{dolarname}')
def historicos(dolarname):
    return Historicoall(dolarname=dolarname)