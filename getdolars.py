import requests
from url import *
from currency import *

dolares_json = []
def Getdolares():
    dolares_json.clear()
    for nombredolar, url in url_dolares.items():
            dolares_json.append(create(requests.get(url).json(),nombredolar))
    return  dolares_json
