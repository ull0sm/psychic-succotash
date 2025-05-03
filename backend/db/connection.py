import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
        host='localhost',
        user='root',           # your MySQL username here
        password='1',   # your MySQL password here
        database='quiz_app'
        )

        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None