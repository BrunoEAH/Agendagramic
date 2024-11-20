import mysql.connector
import mariadb

connection = mariadb.connect(
    user="teste",
    password="teste",
    host="localhost",
    port=3306,
    database="teste"
)