from flask import Flask, render_template, request,abort
from funciones import LeerLibreria

libreria = LeerLibreria()

app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html",libreria=libreria)

@app.route('/libro/<isbn>')
def libro_dinamico(isbn):
	for libro in libreria:
		if libro["isbn"] == isbn:
			return render_template("libro.html",isbn=isbn,libreria=libreria)
	return abort(404)
app.run("0.0.0.0",5000,debug=True)