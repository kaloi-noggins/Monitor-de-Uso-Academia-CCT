from modules import db_crud
from modules.db_init import db_init
from modules.scrapper import get_lotacao
import sqlite3
import threading

db_init()

# tempo em segundos entre as requisiçoes da lotacao da academia
REQUEST_INTERVAL = 60

def salva_lotacao():
    connection = sqlite3.connect("database.db")
    lotacao = get_lotacao()
    print(lotacao)
    db_crud.create(connection, lotacao)
    connection.close()

temporizador = threading.Event()
while not temporizador.wait(REQUEST_INTERVAL):
    salva_lotacao()