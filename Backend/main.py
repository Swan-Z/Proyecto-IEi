from fastapi import FastAPI
from fastapi.responses import JSONResponse
from repositorio import *
# from extractors import extractorCSV as extractor

app = FastAPI()
archivo_csv = 'valenciana.csv'

@app.get('/')
def index():
    return "Hello, World!"

@app.get('/hello')
def consultarUsuarios():
    return Repositorio.fetchData("usuario")

@app.get('/usuario')
def insertarUsuarios(nombre):
    """
    Descripción:
    
    Es una prueba de la fast api 
    """
    data = {
        "nombre": "nombre",
        "password": "world"
    }
    Repositorio.insertData("usuario", data)

# @app.route('/csv', methods=['GET'])
# def csv():
#     try:
#         extractor.csv_a_json()
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)})
 
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
    uvicorn.run(app, host='0.0.0.0', port=7777)