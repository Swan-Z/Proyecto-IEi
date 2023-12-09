import json
import os
import re  
import sys 

ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)
from repositorio import *
from seleniumPrueba import *
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
    rutaJSON = 'jsonResultFromWrapper/CV.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    rutaNuevo = 'jsonResultFromWrapper/CV_Nuevo.json'
    rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))
    generator = SequentialIDGenerator()

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:
            if 'DENOMINACION_GENERICA_ES' in fila:
                fila['nombre'] = fila.pop('DENOMINACION_GENERICA_ES')
            else:
                fila['nombre'] = None
                print('No existe la clave DENOMINACION_GENERICA_ES, por lo tanto esta fila no será insertada')
                print(fila)
            
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
                print('No detecta el tipo')
                print(fila) 
            if 'TIPO_VIA' or 'DIRECCION' or 'NUMERO' in fila:
                fila['direccion'] = str(fila.pop('TIPO_VIA')) + " " + str(fila.pop('DIRECCION')) + ", " + str(fila.pop('NUMERO'))
                direcciones.append(fila['direccion'])
            else:
                fila['direccion'] = None
                print('No existe la dirección, por lo tanto esta fila no será insertada')
                print(fila)
            if 'CODIGO_POSTAL' in fila:
                cp = fila['CODIGO_POSTAL']
                fila['codigo_postal'] = str(cp).zfill(5)  #añadir 0 por delante
                fila['loc.codigo'] = str(cp).zfill(5)
                fila['pro.codigo'] = re.search(r'\d{2}', str(cp).zfill(5)).group()
            else:
                fila['codigo_postal'] = None
                print('No existe la clave CODIGO_POSTAL')
                print(fila)
            if 'TELEFONO' in fila and fila['TELEFONO'] != None:
                if len(str(int(fila['TELEFONO']))) == 9:
                    fila['telefono'] = int(fila.pop('TELEFONO'))
                else:
                    print('Número mayor o menor que 9 dígitos')
                    fila['telefono'] = None
            else:
                fila['telefono'] = None
                print('No existe la clave TELEFONO')
                print(fila)
            if 'URL_ES' in fila:
                fila['descripcion'] = fila.pop('URL_ES')
            else:
                fila['descripcion'] = None
                print('No existe la clave URL_ES')
                print(fila)
            if 'LOCALIDAD' in fila:
                fila['loc.nombre'] = fila.pop('LOCALIDAD')
            else:
                fila['loc.nombre'] = None
                print('No existe la LOCALIDAD')
                print(fila)
            if 'PROVINCIA' in fila:
                fila['pro.nombre'] = fila.pop('PROVINCIA')
            else:
                fila['pro.nombre'] = None
                print('No existe la PROVINCIA')
                print(fila)
    

            datoCentro = {
                'nombre': fila['nombre'],
                'tipo': fila['tipo'],
                'direccion': fila['direccion'],
                'codigo_postal': fila['codigo_postal'],
                'telefono': fila['telefono'],
                'descripcion': fila['descripcion'],
                'longitud': None,
                'latitud': None
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
                'id': generator.generate_id(),
                'nombre': fila['loc.nombre'],
                'en_provincia': fila['pro.nombre']
            }

            datoProvincia = {
                'codigo': fila['pro.codigo'],
                'nombre': fila['pro.nombre'],
            }
            if datoCentro['nombre'] != None and datoCentro['direccion'] != None:
                Repositorio.insertData('Provincia', datoProvincia)
                Repositorio.insertData('Localidad', datoLocalidad)
                Repositorio.insertData('Centro_Educativo', datoCentro) 
            else:
                print(fila)
                print('No ha insertado esta fila porque contiene atributos nulos que no pueden ser nulos')
            
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
