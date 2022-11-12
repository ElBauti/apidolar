from fastapi import FastAPI
import json
import requests

app = FastAPI()

@app.get('/dolardate/turista')
def rutaturista():
    url = 'https://mercados.ambito.com//dolarturista/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Qatar')
def rutaQatar():
    url = 'https://mercados.ambito.com//dolarqatar/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Informal')
def rutaInformal():
    url = 'https://mercados.ambito.com//dolar/informal/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Lujo')
def rutaLujo():
    url = 'https://mercados.ambito.com//dolardelujo/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/ContadoConLiqui')
def rutaContadoConLiqui():
    url = 'https://mercados.ambito.com//dolarrava/cl/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/ColdPlay')
def rutaColdPlay():
    url = 'https://mercados.ambito.com//dolarcoldplay/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Mep')
def rutaMep():
    url = 'https://mercados.ambito.com//dolarrava/mep/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Mayorista')
def rutaMayorista():
    url = 'https://mercados.ambito.com//dolar/mayorista/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Oficial')
def rutaOficial():
    url =  'https://mercados.ambito.com//dolar/oficial/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Ahorra')
def rutaAhorra():
    url = 'https://mercados.ambito.com//dolarahorro/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Futuro')
def rutaFuturo():
    url = 'https://mercados.ambito.com//dolarfuturo/variacion'
    json = requests.get(url).json()
    return json

@app.get('/dolardate/Nacion')
def rutaNacion():
    url = 'https://mercados.ambito.com//dolarnacion//variacion'
    json = requests.get(url).json()
    return json

