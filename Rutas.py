from Urls import *


def dolars():
    nombreDiccionarios = {
    "turista":rutaturista() ,
    "qatar" :rutaqatar(),
    "informal" : rutainformal(),
    "lujo" : rutadelujo(),
    "contadoconliqui" : rutacontadoconliqui() , 
    "coldplay": rutacoldplay(),
    "mep": rutamep(),
    "mayorista": rutamayorista(),
    "oficial": rutaoficial(),
    "ahorro": rutaahorro(),
    "futuro": rutafuturo(),
    "nacion": rutanacion()
}
    return nombreDiccionarios


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
    elif dolarname.lower() == "delujo":
        return rutadelujo()
    elif dolarname.lower() == "informal":
        return rutainformal()
    elif dolarname.lower() == "qatar":  
        return rutaqatar() 
    elif dolarname.lower() == "turista":  
        return rutaturista() 