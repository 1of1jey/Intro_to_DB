import mysql.connector
from mysql.connector import Error


def create_database():
    connection = None
    cursor = None

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host='localhost',        # MySQL server host
        user='root',            # MySQL username
        password='password'     # MySQL password (change as needed)
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")


    except Error as e:
    # Handle any MySQL connection or execution errors
    print(f"Error connecting to MySQL server: {e}")