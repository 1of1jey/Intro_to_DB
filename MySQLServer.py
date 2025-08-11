import mysql.connector
from mysql.connector import Error


def create_database():
    connection = None
    cursor = None