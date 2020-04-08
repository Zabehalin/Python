import psycopg2

if __name__ == "__main__":
    connect_to_db,
    add_user,
    add_valyuts,
    dell_valut,
    vyvid_valut,


def connect_to_db():
    db = psycopg2.connect(
        database="postgres", user="postgres", password="root", host="127.0.0.1", port="5432")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS bank_oop;")
    cursor.execute("USE bank_oop")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), age INT(10), card_number INT(10),pin INT(10),UA FLOAT(10),USD FLOAT(10), EUR FLOAT(10),BTC FLOAT(11)))",
        "CREATE TABLE IF NOT EXISTS curensy (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), age INT(10), card_number INT(10),pin INT(10),UA FLOAT(10),USD FLOAT(10), EUR FLOAT(10),BTC FLOAT(11)))")

    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS valyuts (id INT AUTO_INCREMENT PRIMARY KEY, ccy VARCHAR(255), base_ccy VARCHAR(255), buy FLOAT(10), sale FLOAT(10))", "user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), age INT(10), card_number INT(10),pin INT(10),UA FLOAT(1000),USD FLOAT(1000), EUR FLOAT(1000),BTC FLOAT(10000000000))")

    return db


def dell_valut():
    cursor.execute = "DELETE FROM `valyuts`"
    cursor.execute(sql)
    db.commit()
    #print(cursor.rowcount, "recort del inserted")


def add_valyuts(ccy, base_ccy, buy, sale):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO valyuts (ccy,base_ccy,buy,sale ) VALUES (%s,%s,%s,%s)"
    val = (ccy, base_ccy, buy, sale)
    cursor.execute(sql, val)
    db.commit()
    #print(cursor.rowcount, "Valuyt added")


def vyvid_valut():
    db = connect_to_db()
    cursor = db.cursor()
    sql = "SELECT * FROM valyuts "
    cursor.execute(sql)
    results = cursor.fetchall()
    for item in results:
        print(item)
    #print(cursor.rowcount, "Vyvid stroc")


def add_user(name, surname, age, card_number, pin, UA, USD, EUR, BTC):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO user (name, surname, age, card_number, pin, UA, USD, EUR, BTC) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name, surname, age, card_number, pin, UA, USD, EUR, BTC)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "user added")
