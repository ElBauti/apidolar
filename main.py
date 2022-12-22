from fastapi import FastAPI

from calculadora import Calculadoradolar
from getdolar import Getdolar
from getdolars import Getdolares
from historico import Historicoone
from historicoall import Historicoall
from url import *
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    id: str
    value: str

class Message(BaseModel):
    message: str



@app.get('/getDollar/{dolarname}',
 responses={
        404: {"model": Message, "description": "The item was not found"},
    },
)
def getdolar(dolarname:str):
    try:
        return Getdolar(dolarname)
    except:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get('/getDollars/')
def dolares():
    try:
        return Getdolares()
    except:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get('/calculadora/{compraoventa}/{dolarname}/{dolarunid}')
def calculates(dolarname, dolarunid, compraoventa):
    try:
        return Calculadoradolar(dolarname, dolarunid, compraoventa)
    except:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get('/historicoOne/{dolarname}/{time}')
def historicos(dolarname,time):
    try:
        return Historicoone(dolarname=dolarname,time=time)
    except:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get('/historicoAll/{dolarname}')
def historicos(dolarname):
    try:
        return Historicoall(dolarname=dolarname)
    except:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
