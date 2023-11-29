from flask import Flask, request, jsonify
import requests
from repositorio import *
from extractors import extractorCSV as extractor

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
    try:
        extractor.csv_a_json()
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
 
# @app.route('/csv', methods=['GET'])
# def csv():
#     try:
#         extractor.csv_a_json(archivo_csv, 'nuevo.json')
#         archivo = open('nuevo.json', 'r')
#         data = {
#             "id": "46P01044"
#         }
#         print(data)
#         Repositorio.insertData("Centro_Educativo", data)
#         #return jsonify({"status": "success", "message": "Datos convertidos y guardados correctamente."})
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)