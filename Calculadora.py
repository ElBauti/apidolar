import requests

from url import url_dolares


def calculadoradolar(dolarname:str, dolarunid:int, compraoventa:str):
    DolarAComprar = float(dolarunid)
    for nombredolar, url in url_dolares.items():
        if f"dolar_{dolarname}".lower() == nombredolar:
            dato_dolar = {}
            dato_dolar[nombredolar] = requests.get(url).json()
            if compraoventa == "compra":
                ValorDolarMomento = float(dato_dolar[f'dolar_{dolarname}']["compra"].replace(",","."))
                resultado = DolarAComprar * ValorDolarMomento
            elif compraoventa == "venta":
                ValorDolarMomento = float(dato_dolar[f'dolar_{dolarname}']["venta"].replace(",","."))
                resultado = DolarAComprar * ValorDolarMomento
    return resultado