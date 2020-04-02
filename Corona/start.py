from lib.db import add_corona
import requests

URL = "https://api.covid19api.com/summary"


def menyu(URL):
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


zapov(coron)
