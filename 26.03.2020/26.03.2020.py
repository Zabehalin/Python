import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="countries"
)
cursor = db.cursor()


def zapovnen():
    country = input("Country: ")
    capital = input("Capital: ")
    population = int(input("Population: "))
    mayor = input("Mayor: ")
    sql = "INSERT INTO capitals (country,capital,population,mayor ) VALUES (%s,%s,%s,%s)"
    val = (country, capital, population, mayor)
    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "recort inserted")
    return country, capital, population, mayor


def menyu():
    exit = True
    while exit:
        vyb = int(input("1. NEW Kraina\t0. EXIT    "))
        if vyb == 1:
            zapovnen()
        elif vyb == 0:
            exit = False


menyu()
