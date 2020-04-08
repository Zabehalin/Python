import psycopg2


def connect_to_db():
    conn = psycopg2.connect(database="postgres", user="postgres",
                            password="root", host="127.0.0.1", port="5432")
# =============================== CONECT ========================================

    cursor = conn.cursor()
    name_Table = "Tests"
    sqlCreateTable = "CREATE TABLE " + name_Table + \
        " (id bigint, title varchar(128), summary varchar(256), story text);"
    cursor.execute(sqlCreateTable)
    conn.commit()
    conn.close()
    print("Working")
