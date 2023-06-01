import sqlite3


def create(connection : sqlite3.Connection, lotacao):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO lotacao_academia (lotacao, data) VALUES (? ,?)",
        (lotacao,"DATETIME('now')")
    )

def read(connection: sqlite3.Connection, type: int, type_arg):
    cursor = connection.cursor()

    # type 0  -> select all
    if type == 0:
        cursor.execute('''
            SELECT * FROM lotacao_academia
        ''').fetchall()

def update():
    # nenhum uso ainda
    pass
def delete():
    # nenhum uso ainda
    pass