import mariadb
import sys

def connect_db():
    try:
        conn = mariadb.connect(
            user="root",
            password="mypass",
            host="127.0.0.1",
            port=3306,
            database="takehomeapi"
        )

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        raise

    cur = conn.cursor()
    return cur
