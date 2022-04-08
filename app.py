from re import M
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
        if libro.get("isbn") == isbn:
            nombre = libro.get("title")
            imagen = libro.get("thumbnailUrl")
            paginas = libro.get("pageCount")
            descripcion = libro.get("shortDescription")
            return render_template("libro.html",nombre=nombre,imagen=imagen,paginas=paginas,descripcion=descripcion,isbn=isbn)
    return abort(404)


app.run("0.0.0.0",5000,debug=True)