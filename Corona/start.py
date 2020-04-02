from lib.db import add_corona, dell, vyvid_str
import requests

URL = "https://api.covid19api.com/summary"


def XZ_URL(URL):
    responce = requests.get(URL)
    return responce.json()


coron = requests.get(URL)
coron = coron.json()


def zapov(coron):
    # print(coron)
    for item in coron["Countries"]:
        Country = item["Country"]
        Slug = item["Slug"]
        NewConfirmed = item["NewConfirmed"]
        TotalConfirmed = item["TotalConfirmed"]
        NewDeaths = item["NewDeaths"]
        TotalDeaths = item["TotalDeaths"]
        NewRecovered = item["NewRecovered"]
        TotalRecovered = item["TotalRecovered"]
        add_corona(Country, Slug, NewConfirmed, TotalConfirmed,
                   NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)


def menyu(coron):
    exit = True
    while exit:
        vyb = int(input("1. Vyvesty\t2. Obnovyty\t0. EXIT => "))
        if vyb == 1:
            print("vyv")
            vyvid_str()
        elif vyb == 2:
            print("obnov")
            dell()
            zapov(coron)
        elif vyb == 0:
            exit = False


menyu(coron)
