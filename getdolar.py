import requests
from url import url_dolares
import dateparser
from currency import *


def Getdolar(dolarname):
    for nombredolar, url in url_dolares.items():
        if f'dolar_{dolarname}'.lower() == nombredolar:
            json = create(requests.get(url).json(),nombredolar)
    return  json

