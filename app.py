import sqlite3

from flask import Flask, render_template
from modules import db_crud


# conecção com o banco 
def get_db_connection():
    coonnection = sqlite3.connect("database.db")
    coonnection.row_factory = sqlite3.Row
    return coonnection

# flask app
app = Flask(__name__)

@app.route("/")
def index():
    connection = get_db_connection()
    data = db_crud.read(connection,0,None)
    connection.close()
    return render_template("index.html", data = data)