#Importa la clase Flask del paquete flask
#Clase Mayuscula(Flask) librerias(flask)
from flask import Flask,request,jsonify

app=Flask(__name__)
@app.route('/')
def hello_wordl():
    return '!Hola, mundo¡'

@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar",methods=["GET"])
def sumar():
    num1=int (request.args.get("num1"))
    num2=int (request.args.get("num2"))
    sumar=num1+num2
    if not num1:
        return(
            jsonify({"error":"No hay numero 1"}),
            400,
        )
    elif not num2:
        return(
            jsonify({"error":"No hay numero 2"}),
            400,
        )
    return jsonify({"mensaje":f"La suma es {sumar}"})
@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    if not cadena:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    if cadena == cadena[::-1]:
        mensaje = f'La cadena "{cadena}" es un palíndromo.'
    else:
        mensaje = f'La cadena "{cadena}" no es un palíndromo.'
    return jsonify({"mensaje": mensaje})

@app.route("/contar",methods=["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    if not cadena:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    elif not vocal:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje":f"La cadena tiene:{cadena.count(vocal)} de vocales {vocal}"})  

if __name__=='__main__':
    app.run()
