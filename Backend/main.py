from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
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

@app.get('/mensaje')
def consultarUsuarios():
    return "prueba"

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

from fastapi import FastAPI

app = FastAPI()

@app.get('/busqueda/{nombre_localidad}/{en_provincia}/{codigo_postal}/{tipo}')
def busqueda(
    codigo_postal: str = None,
    en_provincia: str = None,
    nombre_localidad: str = None,
    tipo: str = None
):
    print(codigo_postal)
    print(en_provincia)
    print(nombre_localidad)
    print(tipo)

    # Utiliza los valores de los parámetros como sea necesario
    resultado = Repositorio.fetchBusqueda(
        codigo_postal=codigo_postal,
        en_provincia=en_provincia,
        nombre_localidad=nombre_localidad,
        tipo=tipo
    )
    print('soy resultado', resultado)
    return resultado
    



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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes, ajusta esto según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777)