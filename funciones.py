import json
def LeerLibreria():
    try:
        f=open("books.json")
        datos = json.load(f)
        f.close
        return datos
    except:
        print("error al leer el fichero")