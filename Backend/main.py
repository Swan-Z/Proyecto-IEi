from flask import Flask, request, jsonify
import requests
from repositorio import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello', methods=['GET'])
def consultarUsuarios():
    return Repositorio.fetchData("usuario")

@app.route('/usuario', methods=['GET'])
def insertarUsuarios():
    data = {
        "nombre": "goodmorning",
        "password": "world"
    }
    Repositorio.insertData("usuario", data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)