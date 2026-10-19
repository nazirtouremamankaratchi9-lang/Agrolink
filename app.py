import sqlite3, pickle, base64
from flask import Flask, request

app = Flask(_name_)
DB_PASSWORD = "AgroLink2024!"

def db():
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE produits (id INTEGER, nom TEXT, prix INTEGER)")
    c.execute("INSERT INTO produits VALUES (1,'Manioc',500),(2,'Igname',800)")
    return c

@app.route("/")
def accueil():
    return "AgroLink"

@app.route("/produit")
def produit():
    nom = request.args.get("nom", "")
    rows = db().execute("SELECT * FROM produits WHERE nom = '" + nom + "'").fetchall()
    return str(rows)

@app.route("/bonjour")
def bonjour():
    nom = request.args.get("nom", "")
    return "<h1>Bonjour " + nom + "</h1>"

@app.route("/import", methods=["POST"])
def importer():
    data = base64.b64decode(request.form["data"])
    return str(pickle.loads(data))

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
