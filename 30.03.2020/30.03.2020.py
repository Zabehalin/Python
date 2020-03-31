from lib.db import add_capital, dell_capital, update_capital, vyvid_str


def zapovnen():
    country = input("Country: ")
    capital = input("Capital: ")
    population = int(input("Population: "))
    mayor = input("Mayor: ")
    add_capital(country, capital, population, mayor)


def dellete():
    country = input("Country: ")
    dell_capital(country)


def update():
    Country = input("Country => ")
    stolbic = int(
        input("1. country\t2. capital\t3. population\t 4. mayor => "))
    ADDRES = "test"
    if stolbic == 1:
        ADDRES = "country"
        country = input("Country => ")
        update_capital(Country, country, ADDRES)
    elif stolbic == 2:
        ADDRES = "capital"
        capital = input("Capital => ")
        update_capital(Country, capital, ADDRES)
    elif stolbic == 3:
        ADDRES = "population"
        population = int(input("Population => "))
        update_capital(Country, population, ADDRES)
    elif stolbic == 4:
        ADDRES = "mayor"
        mayor = input("Mayor => ")
        update_capital(Country, mayor, ADDRES)


def vyvid_stroc():
    stroc = input("Enter country => ")
    vyvid_str(stroc)


def menyu():
    exit = True
    while exit:
        vyb = int(
            input("1. NEW Kraina\t2.DEL Kraina\t3. update\t4. Vyvid stroci\t   0. EXIT => "))
        if vyb == 1:
            zapovnen()
        elif vyb == 2:
            dellete()
        elif vyb == 3:
            update()
        elif vyb == 4:
            vyvid_stroc()
        elif vyb == 0:
            exit = False


menyu()
