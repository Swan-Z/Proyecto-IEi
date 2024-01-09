from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from repositorio import *
from fastapi import FastAPI
from extractors import extractorCSV
from extractors import extractorJSON
from extractors import extractorXML

app = FastAPI()
archivo_csv = 'valenciana.csv'

@app.get('/busqueda/{nombre_localidad}/{en_provincia}/{codigo_postal}/{tipo}')
def busqueda(
    codigo_postal: str = None,
    en_provincia: str = None,
    nombre_localidad: str = None,
    tipo: str = None
):
    """Búsqueda de la información de los centros educativos según varios criterios.

    Args: \n
        codigo_postal (str, optional): Código postal del centro educativo. Defaults to None. \n
        en_provincia (str, optional): Nombre de la provincia. Defaults to None. \n
        nombre_localidad (str, optional): Nombre de la localidad. Defaults to None. \n
        tipo (str, optional): Tipo del centro educativo. Defaults to None. \n

    Returns:
        dict: Resultado de la búsqueda.
    """
    resultado = Repositorio.fetchBusqueda(
        codigo_postal=codigo_postal,
        en_provincia=en_provincia,
        nombre_localidad=nombre_localidad,
        tipo=tipo
    )
    return resultado

@app.get('/enviarDatos')
def cargar(
    murcia: bool,
    comunidadValenciana: bool,
    cataluna: bool
):
    datos = {'correctos': 0, 'reparados': [], 'rechazados': []}
    if murcia == True:
         datosMurcia = extractorJSON.json_a_BD()
         datos['correctos'] += datosMurcia['correctos']
         datos['reparados'] += datosMurcia['reparados']
         datos['rechazados'] += datosMurcia['rechazados']
    if cataluna == True:
         datosCataluna = extractorXML.json_a_BD()
         datos['correctos'] += datosCataluna['correctos']
         datos['reparados'] += datosCataluna['reparados']
         datos['rechazados'] += datosCataluna['rechazados']
    if comunidadValenciana == True:
         datoscomunidadValenciana = extractorCSV.json_a_BD()
         datos['correctos'] += datoscomunidadValenciana['correctos']
         datos['reparados'] += datoscomunidadValenciana['reparados']
         datos['rechazados'] += datoscomunidadValenciana['rechazados']
    
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
    return datos
    #return {'correctos': 7, 'reparados': ['hello', 'how are you', 'im fine, thank you'], 'rechazados': ['hasta aqui, adios']}
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes, ajusta esto según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777)