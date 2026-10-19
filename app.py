import os, re, json, sqlite3
from flask import Flask, request, abort
from markupsafe import escape

app = Flask(_name_)
# Le secret vient de l'environnement, jamais du code
DB_PASSWORD = os.environ.get("DB_PASSWORD")

NOM_VALIDE = re.compile(r"^[A-Za-zÀ-ÿ '\-]{1,50}$")

def nom_valide(nom):
    if not NOM_VALIDE.fullmatch(nom):
        abort(400, "Nom invalide")
    return nom

def db():
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE produits (id INTEGER, nom TEXT, prix INTEGER)")
    c.execute("INSERT INTO produits VALUES (1,'Manioc',500),(2,'Igname',800)")
    return c

@app.route("/")
def accueil():
    return "AgroLink"


