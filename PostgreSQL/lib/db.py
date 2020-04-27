import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
if __name__ == "__main__":
    connect_to_db,


def connect_to_db():
    conn = psycopg2.connect(database="test", user="postgres",
                            password="root", host="127.0.0.1", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = conn.cursor()
    #sqll = "CREATE DATABASE test"
    sql = "CREATE TABLE IF NOT EXISTS account(cardnumber serial PRIMARY KEY,name VARCHAR(50) NOT NULL,surname VARCHAR(50) NOT NULL,amount FLOAT(10) NOT NULL,currancy VARCHAR (10) NOT NULL)"
    cursor.execute(sql)
    conn.commit()
    print("Working")
    return conn
