import mysql.connector
if __name__ == "__main__":
    connect_to_db,
    add_capital,
    dell_capital,
    update_capital


def connect_to_db():
    db = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="countries")

    return db


def add_capital(country, capital, population, mayor):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO capitals (country,capital,population,mayor ) VALUES (%s,%s,%s,%s)"
    val = (country, capital, population, mayor)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "Capital added")


def dell_capital(country):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "DELETE FROM `capitals` WHERE country=country"
    val = (country)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "recort del inserted")


def update_capital(Country, stolbic, ADDRES):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "UPDATE capitals SET ADDRES = '" + \
        stolbic + "' WHERE country='" + Country + "'"
    val = (Country, stolbic, ADDRES)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "Update stolbic")
