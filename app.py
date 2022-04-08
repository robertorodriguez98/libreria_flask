from flask import Flask, render_template, request
from funciones import LeerLibreria

libreria = LeerLibreria()

app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html",libreria=libreria)

app.run("0.0.0.0",5000,debug=True)