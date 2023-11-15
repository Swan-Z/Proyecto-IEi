from flask import Flask, request, jsonify
import requests
from repositorio import *
from extractors import extractorCSV as e

app = Flask(__name__)
archivo_csv = 'valenciana.csv'

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


@app.route('/csv', methods=['GET'])
def csv():
    e.csv_a_json(archivo_csv,'nuevo.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)