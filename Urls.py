import requests

url_source = "https://mercados.ambito.com/"

def rutaturista():
    url =f'{url_source}/dolarturista/variacion'
    json = requests.get(url).json()
    return json
    

def rutaqatar():
    url = f'{url_source}/dolarqatar/variacion'
    json = requests.get(url).json()
    return json
    

def rutainformal():
    url = f"{url_source}/dolar/informal/variacion"
    json = requests.get(url).json()
    return json
    

def rutadelujo():
    
    url = f"{url_source}/dolardelujo/variacion"
    json = requests.get(url).json()
    return json
    


def rutacontadoconliqui():
    url = f"{url_source}/dolarrava/cl/variacion"
    json = requests.get(url).json()
    return json
    


def rutacoldplay():
    url = f"{url_source}/dolarcoldplay/variacion"
    json = requests.get(url).json()
    return json
    


def rutamep():
    url = f"{url_source}/dolarrava/mep/variacion"
    json = requests.get(url).json()
    return json
    


def rutamayorista():
    url = f"{url_source}/dolar/mayorista/variacion"
    json = requests.get(url).json()
    return json
    


def rutaoficial():
    url =  f"{url_source}/dolar/oficial/variacion"
    json = requests.get(url).json()
    return json
    


def rutaahorro():
    url = f"{url_source}/dolarahorro/variacion"
    json = requests.get(url).json()
    return json
    


def rutafuturo():
    url = f"{url_source}/dolarfuturo/variacion"
    json = requests.get(url).json()
    return json
    


def rutanacion():
    url = f"{url_source}/dolarnacion/variacion"
    json = requests.get(url).json()
    return  json    
    
