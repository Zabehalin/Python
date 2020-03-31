from lib.db import add_valyuts

import requests

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def request(URL):
    responce = requests.get(URL)
    return responce.json()


cuurency = request(URL)


def zapov(cuurency):
    for item in cuurency:
        ccy = str(item["ccy"])
        base_ccy = str(item["base_ccy"])
        buy = float(item["buy"])
        sale = float(item["sale"])
        add_valyuts(ccy, base_ccy, buy, sale)


zapov(cuurency)
