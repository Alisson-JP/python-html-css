import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "minhasenha"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def pos_requisicao(exception):
    g.bd.close()

@app.route('/')
def index():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo': titulo, 'texto': texto})
    return str(entradas)

@app.route('/batera')
def batera():
    return "<h1 style='color:red;'>Toco bateria desde os 13 anos!</h1>"




