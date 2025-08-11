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