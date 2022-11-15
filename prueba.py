lista = [1, 2, 3, 4, 5]

a =  lista[-3:]
b =   lista[:-3]
c = lista[-3]
d = lista[::-3]
print(False or False or True)
print('false' or () or [])
print((1,) or False or [])
print(() or {} or [])

import requests

def rutaLujo(dolar_name ='qatar'):
    url = f'https://mercados.ambito.com//dolar{dolar_name}/variacion'
    print(url)
    json = requests.get(url).json()
    return json

rutaLujo()