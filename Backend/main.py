from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from repositorio import *
from fastapi import FastAPI
# from extractors import extractorCSV as extractor

app = FastAPI()
archivo_csv = 'valenciana.csv'

@app.get('/busqueda/{nombre_localidad}/{en_provincia}/{codigo_postal}/{tipo}')
def busqueda(
    codigo_postal: str = None,
    en_provincia: str = None,
    nombre_localidad: str = None,
    tipo: str = None
):
    resultado = Repositorio.fetchBusqueda(
        codigo_postal=codigo_postal,
        en_provincia=en_provincia,
        nombre_localidad=nombre_localidad,
        tipo=tipo
    )
    return resultado

@app.get('/enviarDatos')
def cargar(
    selectAll: bool,
    murcia: bool,
    comunidadValenciana: bool,
    cataluna: bool
):
    # if murcia ==True:
    #     return murcia
    # if cataluna == True: 
    #     return cataluna
    
    return {'correctos': 7, 'reparados': ['hello', 'how are you', 'im fine, thank you'], 'rechazados': ['hasta aqui, adios']}
    



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