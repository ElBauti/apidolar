import requests


def historicocontent(urldata,time,dolarname):
        
        if dolarname.lower() == "turista" or dolarname.lower() == "qatar" or dolarname.lower() == "delujo" or dolarname.lower() == "coldplay" or dolarname.lower() == "ahorro" or dolarname.lower() == "nacion":
            urltime = f'https://mercados.ambito.com//dolar{dolarname}/grafico/{time}'
            jsondata = requests.get(urldata).json()
            jsontime = requests.get(urltime).json()
            urls = {'valores':jsondata,f'historico_{time}':jsontime}
            return urls

        elif dolarname.lower() == "informal" or dolarname.lower() == "mayorista" or dolarname.lower() == "oficial":
                urltime = f'https://mercados.ambito.com//dolar/{dolarname}/grafico/{time}'
                jsondata = requests.get(urldata).json()
                jsontime = requests.get(urltime).json()
                urls = {'valores':jsondata,f'historico_{time}':jsontime}
                return urls

        elif dolarname.lower() == "mep" or dolarname.lower() == "contadoconliqui":
            if dolarname.lower() == "mep":
                urltime = f'https://mercados.ambito.com//dolarrava/mep/grafico/{time}'
                jsondata = requests.get(urldata).json()
                jsontime = requests.get(urltime).json()
                urls = {'valores':jsondata,f'historico_{time}':jsontime}
                return urls
            else:
                urltime = f'https://mercados.ambito.com//dolarrava/cl/grafico/{time}'
                jsondata = requests.get(urldata).json()
                jsontime = requests.get(urltime).json()
                urls = {'valores':jsondata,f'historico_{time}':jsontime}
                return urls

        elif dolarname.lower() == "futuro":
                urltime = 'https://mercados.ambito.com//dolarfuturo/datos'
                jsondata = requests.get(urldata).json()
                jsontime = requests.get(urltime).json()
                urls = {'valores':jsondata,f'historico_{time}':jsontime}
                return urls
        else:
            return "ERROR 404 NOT FOUND"


            



def historico(dolarname,time):
    if dolarname.lower() == "turista":
        return historicocontent('https://mercados.ambito.com//dolarturista/variacion',time,dolarname)
    elif dolarname.lower() == "qatar":
        return historicocontent('https://mercados.ambito.com//dolarqatar/variacion',time,dolarname)
    elif dolarname.lower() == "delujo":
        return historicocontent('https://mercados.ambito.com//dolardelujo/variacion',time,dolarname)
    elif dolarname.lower() == "ahorro":
        return historicocontent('https://mercados.ambito.com//dolarahorro/variacion',time,dolarname)
    elif dolarname.lower() == "nacion":
        return historicocontent('https://mercados.ambito.com//dolarnacion/variacion',time,dolarname)
    elif dolarname.lower() == "coldplay":
        return historicocontent('https://mercados.ambito.com//dolarcoldplay/variacion',time,dolarname)
    elif dolarname.lower() == "informal":
        return historicocontent('https://mercados.ambito.com//dolar/informal/variacion',time,dolarname)    
    elif dolarname.lower() == "oficial":
        return historicocontent('https://mercados.ambito.com//dolar/oficial/variacion',time,dolarname)
    elif dolarname.lower() == "mayorista":
        return historicocontent('https://mercados.ambito.com//dolar/mayorista/variacion',time,dolarname)
    elif dolarname.lower() == "mep":
        return historicocontent('https://mercados.ambito.com//dolarrava/mep/variacion',time,dolarname)
    elif dolarname.lower() == "contadoconliqui":
        return historicocontent('https://mercados.ambito.com//dolarrava/cl/variacion',time,dolarname)    
    elif dolarname.lower() == "futuro":
        return historicocontent('https://mercados.ambito.com//dolarfuturo/variacion',time,dolarname)    

