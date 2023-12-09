import json
import os
import re  
import sys 
import logging

ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)
from repositorio import *
from seleniumPrueba import *
logging.basicConfig(level=logging.WARNING)

class Colores:
    RESET = '\033[0m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
# from wrappers.wrapperXML import *

# def csv_a_json():
#     directorio_actual = os.getcwd()
#     rutaCSVOriginal = 'ficheroFuenteDatos/CV.csv'
#     rutaJSON = 'jsonResultFromWrapper/CV.json'
#     rutaComCSV = os.path.abspath(os.path.join(directorio_actual, rutaCSVOriginal))
#     rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
#     wrapperXML_to_JSON(rutaComCSV, rutaComJSON)
class SequentialIDGenerator:
    def __init__(self):
        self.counter = 0

    def generate_id(self):
        self.counter += 1
        return self.counter

def json_a_BD():
    datos_centro = []
    datos_localidad = []
    datos_provincia = []
    direcciones = []
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/CV_demo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    rutaNuevo = 'jsonResultFromWrapper/CV_Nuevo.json'
    rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:
            if 'DENOMINACION_GENERICA_ES' in fila and fila['DENOMINACION_GENERICA_ES'] is not None and fila['DENOMINACION_GENERICA_ES'] != '':
                fila['nombre'] = fila.pop('DENOMINACION_GENERICA_ES')
            else:
                fila['nombre'] = None
                print(Colores.ROJO + 'No existe la clave DENOMINACION_GENERICA_ES, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
            
            if 'REGIMEN' in fila:
                if fila['REGIMEN'] == 'PRIV.':
                    fila['tipo'] = 'Privado'
                elif fila['REGIMEN'] == 'PÚB.':
                    fila['tipo'] = 'Público'
                elif fila['REGIMEN'] == 'PRIV. CONC.':
                    fila['tipo'] = 'Concertado'
                elif fila['REGIMEN'] == 'OTROS':
                    fila['tipo'] = 'Otros'
            else:
                fila['tipo'] = 'Otros'
                print(Colores.AMARILLO + 'No se ha podido determinar el tipo de centro: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)
            if 'TIPO_VIA' or 'DIRECCION' or 'NUMERO' in fila:
                fila['direccion'] = str(fila.pop('TIPO_VIA')) + " " + str(fila.pop('DIRECCION')) + ", " + str(fila.pop('NUMERO'))
                direcciones.append(fila['direccion'])
            else:
                fila['direccion'] = None
                print(Colores.ROJO + 'No existe la dirección, por lo tanto esta fila no será insertada: '+ Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
            if 'CODIGO_POSTAL' in fila and fila['CODIGO_POSTAL'] is not None and fila['CODIGO_POSTAL'] != '':
                cp = fila['CODIGO_POSTAL']
                fila['codigo_postal'] = str(cp).zfill(5)  #añadir 0 por delante
                fila['loc.codigo'] = str(cp).zfill(5)
                fila['pro.codigo'] = re.search(r'\d{2}', str(cp).zfill(5)).group()
            else:
                fila['codigo_postal'] = None
                print(Colores.ROJO + 'No existe la clave CODIGO_POSTAL, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
            if 'TELEFONO' in fila and fila['TELEFONO'] != None:
                if len(str(int(fila['TELEFONO']))) == 9:
                    fila['telefono'] = int(fila.pop('TELEFONO'))
                else:
                    print(Colores.AMARILLO +'Número con formato erroneo: ' + Colores.RESET)
                    print(Colores.AMARILLO + str(fila) + Colores.RESET)
                    fila['telefono'] = None
            else:
                fila['telefono'] = None
                print(Colores.AMARILLO + 'No existe la clave TELEFONO: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)
            if 'URL_ES' in fila:
                fila['descripcion'] = fila.pop('URL_ES')
            else:
                fila['descripcion'] = None
                print(Colores.AMARILLO + 'No existe la clave URL_ES: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)
            if 'LOCALIDAD' in fila and fila['LOCALIDAD'] is not None and fila['LOCALIDAD'] != '':
                fila['loc.nombre'] = fila.pop('LOCALIDAD')
            else:
                fila['loc.nombre'] = None
                print(Colores.ROJO + 'No existe la clave LOCALIDAD, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
            if 'PROVINCIA' in fila and fila['PROVINCIA'] is not None and fila['PROVINCIA'] != '':
                fila['pro.nombre'] = fila.pop('PROVINCIA')
            else:
                fila['pro.nombre'] = None
                print(Colores.ROJO + 'No existe la clave PROVINCIA, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
    

            datoCentro = {
                'nombre': fila['nombre'],
                'tipo': fila['tipo'],
                'direccion': fila['direccion'],
                'codigo_postal': fila['codigo_postal'],
                'telefono': fila['telefono'],
                'descripcion': fila['descripcion'],
                'longitud': None,
                'latitud': None,
                'id_localidad' : ''
            }
            dir = str(fila['direccion']) + ", " + str(fila['loc.nombre']) + ", " + str(fila['codigo_postal'])
            print(dir)
            # direcciones.append(dir)  para que sea más rápido con una ventana de buscador abierta continuament
            res = verificar_titulo(dir)
            print(res)
            datoCentro['longitud'] = res['longitud']
            datoCentro['latitud'] = res['latitud']
            res = {
                'longitud': datoCentro['longitud'],
                'latitud': datoCentro['latitud']
            }
            

            datoLocalidad = {
                'nombre': fila['loc.nombre'],
                'en_provincia': fila['pro.nombre']
            }

            datoProvincia = {
                'codigo': fila['pro.codigo'],
                'nombre': fila['pro.nombre'],
            }

            if datoCentro['nombre'] and datoCentro['direccion'] and datoCentro['longitud'] and datoCentro['latitud'] and datoCentro['codigo_postal']:
                Repositorio.insertData('Provincia', datoProvincia)
                Repositorio.insertData('Localidad', datoLocalidad)
                datoCentro['id_localidad'] = Repositorio.fetchDataByNames('Localidad', datoLocalidad['nombre'])[0]['id']
                Repositorio.insertData('Centro_Educativo', datoCentro) 
            else:
                print('')
            
            datos_centro.append(datoCentro)

        # res = verificar_titulo(direcciones)
        # for i in res:
        #     geo = {
        #         'longitud': i['longitud'],
        #         'latitud': i['latitud']
        #     }
        #     Repositorio.insertData('Centro_Educativo', geo)

        
        

        with open(rutaComNuevo, 'w', encoding='utf-8') as archivoNuevo:
            json.dump(datos_centro, archivoNuevo, indent=2, ensure_ascii=False)
        
# csv_a_json()
json_a_BD()
