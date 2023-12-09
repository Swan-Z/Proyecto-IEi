import json
import os
import re  
import sys 
import logging

ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)
logging.basicConfig(level=logging.WARNING)
from repositorio import *

class Colores:
    RESET = '\033[0m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
# from wrappers.wrapperXML import *

# def xml_a_json():
#     directorio_actual = os.getcwd()
#     rutaXMLOriginal = 'ficheroFuenteDatos/CAT.xml'
#     rutaJSON = 'jsonResultFromWrapper/CAT.json'
#     rutaComXML = os.path.abspath(os.path.join(directorio_actual, rutaXMLOriginal))
#     rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
#     wrapperXML_to_JSON(rutaComXML, rutaComJSON)

def json_a_BD():
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/CAT_demo.json'
    # rutaNuevo = 'jsonResultFromWrapper/CAT_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    # rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:

             # Renombrar claves si existen
            if 'denominaci_completa' in fila['row'] and fila['row']['denominaci_completa'] is not None and fila['row']['denominaci_completa'] != '':
                fila['nombre'] = fila['row'].pop('denominaci_completa')
            else:  
                fila['nombre'] = None
                print(Colores.ROJO + 'No existe la clave denominaci_completa, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)

            if 'nom_naturalesa' in fila['row']:
                if 'concertat' in fila['row']['nom_naturalesa'].lower():
                    fila['tipo'] = 'Concertado'
                else:
                    if 'privat' in fila['row']['nom_naturalesa'].lower():
                        fila['tipo'] = 'Privado'
                    elif 'públic' in fila['row']['nom_naturalesa'].lower():
                        fila['tipo'] = 'Público'
                    else:
                        print(Colores.AMARILLO + 'No se ha podido determinar el tipo de centro: ' + Colores.RESET)
                        print(Colores.AMARILLO + str(fila) + Colores.RESET)
                        fila['tipo'] = 'Otros'
            else:
                fila['tipo'] = 'Otros'
                print(Colores.AMARILLO + 'No existe la clave nom_naturalesa: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)


            if 'adre_a' in fila['row'] and fila['row']['adre_a'] is not None and fila['row']['adre_a'] != '':
                fila['direccion'] = fila['row'].pop('adre_a')
            else:
                fila['direccion'] = None
                print(Colores.ROJO + 'No existe la dirección, por lo tanto esta fila no será insertada: '+ Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                
            if 'codi_postal' in fila['row'] and fila['row']['codi_postal'] is not None and fila['row']['codi_postal'] != '':
                fila['codigo_postal'] = fila['row'].pop('codi_postal')
                fila['codigo_provincia'] = fila['codigo_postal'][:2]
            else:
                fila['codigo_provincia'] = None
                fila['codigo_postal'] = None
                fila['nombre_provincia'] = None
                print(Colores.ROJO + 'No existe la clave codi_postal, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                    
            if 'estudis' in fila['row']:
                fila['descripcion'] = fila['row'].pop('estudis')
            else:
                fila['descripcion'] = None
                print(Colores.AMARILLO + 'No existe la clave estudis: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)

            # Mover datos de georeferencia si existen

            if 'coordenades_geo_x' in fila['row'] and fila['row']['coordenades_geo_x'] is not None and fila['row']['coordenades_geo_x'] != '':
                    fila['longitud'] = fila['row'].pop('coordenades_geo_x')
            else:
                    fila['longitud'] = None
                    print(Colores.ROJO + 'No existe la clave coordenades_geo_x por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
            if 'coordenades_geo_y' in fila['row'] and fila['row']['coordenades_geo_y'] is not None and fila['row']['coordenades_geo_y'] != '':
                    fila['latitud'] = fila['row'].pop('coordenades_geo_y')
            else:
                    fila['latitud'] = None
                    print(Colores.ROJO + 'No existe la clave coordenades_geo_y por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
            #-----------------------------------------------------------------
            if 'nom_municipi' in fila['row'] and fila['row']['nom_municipi'] is not None and fila['row']['nom_municipi'] != '':
                fila['localidad'] = fila['row'].pop('nom_municipi')
            else:
                print(Colores.ROJO + 'No existe la clave nom_municipi, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
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
                    print(Colores.AMARILLO + 'No se ha podido determinar la provincia' + Colores.RESET)
                    print(Colores.AMARILLO + str(fila) + Colores.RESET)
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
                'id_localidad' : ''
            }

            datoProvincia = {
                'codigo': fila['codigo_provincia'],
                'nombre': fila['nombre_provincia']
            }
                

            datoLocalidad = {
                'nombre': fila['localidad'],
                'en_provincia': fila['nombre_provincia']
            } 

            if datoCentro['nombre'] != None and datoCentro['direccion'] != None and datoCentro['longitud'] != None and datoCentro['latitud'] != None:
                Repositorio.insertData('Provincia', datoProvincia)
                Repositorio.insertData('Localidad', datoLocalidad)
                datoCentro['id_localidad'] = Repositorio.fetchDataByNames('Localidad', datoLocalidad['nombre'])[0]['id']
                Repositorio.insertData('Centro_Educativo', datoCentro)
            else:
                print('')

# xml_a_json()
json_a_BD()
