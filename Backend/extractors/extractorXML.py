import json
import os
import re  
import sys 

ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)

from repositorio import *
# from wrappers.wrapperXML import *

# def xml_a_json():
#     directorio_actual = os.getcwd()
#     rutaXMLOriginal = 'ficheroFuenteDatos/CAT.xml'
#     rutaJSON = 'jsonResultFromWrapper/CAT.json'
#     rutaComXML = os.path.abspath(os.path.join(directorio_actual, rutaXMLOriginal))
#     rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
#     wrapperXML_to_JSON(rutaComXML, rutaComJSON)
class SequentialIDGenerator:
    def __init__(self):
        self.counter = 0

    def generate_id(self):
        self.counter += 1
        return self.counter
  

def json_a_BD():
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/CAT.json'
    # rutaNuevo = 'jsonResultFromWrapper/CAT_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    # rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))
    generator = SequentialIDGenerator()

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:

             # Renombrar claves si existen
            if 'denominaci_completa' in fila['row']:
                fila['nombre'] = fila['row'].pop('denominaci_completa')
            else:  
                fila['nombre'] = None
                print('No existe la clave denominaci_completa, por lo tanto esta fila no será insertada')
                print(fila)

            if 'nom_naturalesa' in fila['row']:
                if 'concertat' in fila['row']['nom_naturalesa'].lower():
                    fila['tipo'] = 'Concertado'
                else:
                    if 'privat' in fila['row']['nom_naturalesa'].lower():
                        fila['tipo'] = 'Privado'
                    elif 'públic' in fila['row']['nom_naturalesa'].lower():
                        fila['tipo'] = 'Público'
                    else:
                        print('No se ha podido determinar el tipo de centro')
                        print(fila)
                        fila['tipo'] = 'Otros'
            else:
                fila['tipo'] = 'Otros'
                print('No existe la clave tipo')
                print(fila)


            if 'adre_a' in fila['row']:
                fila['direccion'] = fila['row'].pop('adre_a')
            else:
                fila['direccion'] = None
                print('No existe la dirección, por lo tanto esta fila no será insertada')
                print(fila)
                
            if 'codi_postal' in fila['row']:
                fila['codigo_postal'] = fila['row'].pop('codi_postal')
                fila['codigo_provincia'] = fila['codigo_postal'][:2]
            else:
                fila['codigo_provincia'] = None
                fila['codigo_postal'] = None
                fila['nombre_provincia'] = None
                print('No existe la clave codi_postal')
                print(fila)
                
            
                
            if 'estudis' in fila['row']:
                fila['descripcion'] = fila['row'].pop('estudis')
            else:
                fila['descripcion'] = None
                print('No existe la clave estudis')
                print(fila)

            # Mover datos de georeferencia si existen

            if 'coordenades_geo_x' in fila['row']:
                    fila['longitud'] = fila['row'].pop('coordenades_geo_x')
            else:
                    fila['longitud'] = None
                    print('No existe la clave longitud')
                    print(fila)
            if 'coordenades_geo_y' in fila['row']:
                    fila['latitud'] = fila['row'].pop('coordenades_geo_y')
            else:
                    fila['latitud'] = None
                    print('No existe la clave latitud')
                    print(fila)
            #-----------------------------------------------------------------
            if 'nom_municipi' in fila['row']:
                fila['localidad'] = fila['row'].pop('nom_municipi')
            else:
                print('No existe la clave nom_municipi')
                print(fila)
                fila['localidad'] = None
            if fila['codigo_provincia'] != None:
                if fila['codigo_provincia'] == '08':
                    fila['nombre_provincia'] = 'Barcelona'
                elif fila['codigo_provincia'] == '17':
                    fila['nombre_provincia'] = 'Girona'
                elif fila['codigo_provincia'] == '25':
                    fila['nombre_provincia'] = 'Lleida'
                elif fila['codigo_provincia'] == '43':
                    fila['nombre_provincia'] = 'Tarragona'
                else:
                    print('No se ha podido determinar la provincia')
                    print(fila)
                    fila['nombre_provincia'] = None

            #-----------------------------------------------------------------

            datoCentro = {
                'nombre': fila['nombre'],
                'tipo': fila['tipo'],
                'direccion': fila['direccion'],
                'codigo_postal': fila['codigo_postal'],
                'telefono': None,
                'descripcion': fila['descripcion'],
                'longitud': fila['longitud'],
                'latitud': fila['latitud'],
            }

            datoProvincia = {
                'codigo': fila['codigo_provincia'],
                'nombre': fila['nombre_provincia']
            }
                

            datoLocalidad = {
                'id': generator.generate_id(),
                'nombre': fila['localidad'],
                'en_provincia': fila['nombre_provincia']
            } 

            if datoCentro['nombre'] != None and datoCentro['direccion'] != None:
                Repositorio.insertData('Provincia', datoProvincia)
                Repositorio.insertData('Localidad', datoLocalidad)
                Repositorio.insertData('Centro_Educativo', datoCentro)
            else:
                print(fila)
                print('No ha insertado esta fila porque contiene atributos nulos que no pueden ser nulos')

# xml_a_json()
json_a_BD()
