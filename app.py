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
            publicado = libro.get("status")
            nombre = libro.get("title")
            imagen = libro.get("thumbnailUrl")
            paginas = libro.get("pageCount")
            autores = libro.get("authors")
            descripcion = libro.get("shortDescription")
            categorias = libro.get("categories")
            return render_template("libro.html",nombre=nombre,imagen=imagen,paginas=paginas,autores=autores,descripcion=descripcion,categorias=categorias,publicado=publicado,isbn=isbn)
    return abort(404)


app.run("0.0.0.0",5000,debug=True)