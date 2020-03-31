import mysql.connector

if __name__ == "__main__":
    connect_to_db,
    add_valyuts


def connect_to_db():
    db = mysql.connector.connect(host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS obmin_valyut;")
    cursor.execute("USE obmin_valyut")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS valyuts (id INT AUTO_INCREMENT PRIMARY KEY, ccy VARCHAR(255), base_ccy VARCHAR(255), buy FLOAT(10), sale FLOAT(10))")

    return db


def add_valyuts(ccy, base_ccy, buy, sale):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO valyuts (ccy,base_ccy,buy,sale ) VALUES (%s,%s,%s,%s)"
    val = (ccy, base_ccy, buy, sale)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "Valuyt added")
