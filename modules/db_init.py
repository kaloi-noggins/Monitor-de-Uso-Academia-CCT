import sqlite3
import psycopg2

def db_init():
    
    # le o schema e inicializa o banco
    connection = sqlite3.connect("database.db")

    with open("./resources/schema.sql") as f:
        connection.executescript(f.read()) 