import mysql.connector

if __name__ == "__main__":
    connect_to_db,
    add_corona,
    dell,
    vyvid_str


def connect_to_db():
    db = mysql.connector.connect(host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS corona_virus;")
    cursor.execute("USE corona_virus")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS CORON (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10),NewDeaths INT(10),TotalDeaths INT(10),NewRecovered INT(10),TotalRecovered INT(10))")

    return db


def add_corona(Country, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO CORON (Country,Slug,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (Country, Slug, NewConfirmed, TotalConfirmed,
           NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "Coron added")


def dell():
    db = connect_to_db()
    cursor = db.cursor()
    sql = "DELETE FROM `coron`"
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount, "recort del inserted")


def vyvid_str():
    db = connect_to_db()
    cursor = db.cursor()
    sql = "SELECT Country , TotalConfirmed FROM coron ORDER BY TotalConfirmed"
    cursor.execute(sql)
    results = cursor.fetchall()
    for item in results:
        print(item)
    print(cursor.rowcount, "Vyvyd stroc")
