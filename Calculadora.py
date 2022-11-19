from Rutas import dolaruta


def calculate(dolarname:str, dolarunid:int, compraoventa:str):
    print("Hola")
    dolardato = dolaruta(dolarname)
    DolarAComprar = float(dolarunid)
    if compraoventa.lower() == 'compra':
        ValorDolarMomento = float(dolardato["compra"].replace(",","."))
        resultado = DolarAComprar * ValorDolarMomento
        return resultado
    elif compraoventa.lower() == 'venta':
        ValorDolarMomento = float(dolardato["venta"].replace(",","."))
        resultado = DolarAComprar * ValorDolarMomento
        return resultado
    else:
        return "ERROR 404"