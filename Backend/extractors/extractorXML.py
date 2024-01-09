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
    resultado = {
         'correctos': 0,
         'reparados': [],
         'rechazados': [],
    }
    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        # En este for se recorre cada fila del JSON y se van incorporando las filas a la base de datos como corresponde, 
        # tambien se gestionan los errores que puedan surgir
        for fila in lector_json:
            reparado=False
            rechazado=False
            error = 'Cataluña, '
            motivo = ''
            arreglo = ''
            # Aqui se recupera el valor de la clave denominaci_completa y se le asigna a la clave nombre
            if 'denominaci_completa' in fila['row'] and fila['row']['denominaci_completa'] is not None and fila['row']['denominaci_completa'] != '':
                fila['nombre'] = fila['row'].pop('denominaci_completa')
            else:  
                fila['nombre'] = ''
                print(Colores.ROJO + 'No existe la clave denominaci_completa, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                rechazado=True
                motivo += 'no tiene nombre. '
            # Aqui se recupera el valor de la clave nom_naturalesa y se le asigna a la clave tipo
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
                        reparado=True
                        motivo += 'no se ha podido determinar el tipo de centro, '
                        arreglo += 'se le ha asignado el tipo Otros.'
            else:
                fila['tipo'] = 'Otros'
                print(Colores.AMARILLO + 'No existe la clave nom_naturalesa: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)
                reparado=True
                motivo += 'no se ha podido determinar el tipo de centro, '
                arreglo += 'se le ha asignado el tipo Otros.'

            # Aqui se recupera el valor de la clave adre_a y se le asigna a la clave direccion
            if 'adre_a' in fila['row'] and fila['row']['adre_a'] is not None and fila['row']['adre_a'] != '':
                fila['direccion'] = fila['row'].pop('adre_a')
            else:
                fila['direccion'] = ''
                print(Colores.ROJO + 'No existe la dirección, por lo tanto esta fila no será insertada: '+ Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                rechazado=True
                motivo += 'no tiene dirección. '
            # Aqui se recupera el valor de la clave codi_postal y se le asigna a la clave codigo_postal
            if 'codi_postal' in fila['row'] and fila['row']['codi_postal'] is not None and fila['row']['codi_postal'] != '':
                fila['codigo_postal'] = fila['row'].pop('codi_postal')
                fila['codigo_provincia'] = fila['codigo_postal'][:2]
            else:
                fila['codigo_provincia'] = None
                fila['codigo_postal'] = None
                fila['nombre_provincia'] = None
                print(Colores.ROJO + 'No existe la clave codi_postal, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                rechazado=True
                motivo += 'no tiene código postal. '
            # Aqui se recupera el valor de la clave estudis y se le asigna a la clave descripcion        
            if 'estudis' in fila['row']:
                fila['descripcion'] = fila['row'].pop('estudis')
            else:
                fila['descripcion'] = None
                print(Colores.AMARILLO + 'No existe la clave estudis: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)

            # Mover datos de georeferencia si existen
            # Aqui se recupera el valor de la clave coordenades_geo_x y se le asigna a la clave longitud
            if 'coordenades_geo_x' in fila['row'] and fila['row']['coordenades_geo_x'] is not None and fila['row']['coordenades_geo_x'] != '':
                    fila['longitud'] = fila['row'].pop('coordenades_geo_x')
            else:
                    fila['longitud'] = None
                    print(Colores.ROJO + 'No existe la clave coordenades_geo_x por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
                    rechazado=True
                    motivo += 'no tiene longitud. '
            # Aqui se recupera el valor de la clave coordenades_geo_y y se le asigna a la clave latitud
            if 'coordenades_geo_y' in fila['row'] and fila['row']['coordenades_geo_y'] is not None and fila['row']['coordenades_geo_y'] != '':
                    fila['latitud'] = fila['row'].pop('coordenades_geo_y')
            else:
                    fila['latitud'] = None
                    print(Colores.ROJO + 'No existe la clave coordenades_geo_y por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
                    rechazado=True
                    motivo += 'no tiene latitud. '
            #-----------------------------------------------------------------
            # Aqui se recupera el valor de la clave nom_municipi y se le asigna a la clave localidad
            if 'nom_municipi' in fila['row'] and fila['row']['nom_municipi'] is not None and fila['row']['nom_municipi'] != '':
                fila['localidad'] = fila['row'].pop('nom_municipi')
            else:
                print(Colores.ROJO + 'No existe la clave nom_municipi, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                fila['localidad'] = ''
                rechazado=True
                motivo += 'no tiene localidad. '
            # Aqui se recupera el valor de la clave codigo_provincia y se le asigna a la clave nombre_provincia segun el codigo de provincia
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
            # Aqui se comprueba si la fila ha sido rechazada
            if not rechazado:
                # Aqui se comprueba si la fila ha sido reparada, y se inserta el string correspondiente del aviso de esto, y 
                # se comprueban tambien que no esten ya en la base de datos los datos que se van a insertar
                if reparado:
                    resultado['reparados'].append(error + datoCentro['nombre'] + ', ' + datoLocalidad['nombre'] + ', ' + motivo + arreglo)
                if Repositorio.fetchDataByNames('provincia', datoProvincia['nombre']) == []:
                    Repositorio.insertData('provincia', datoProvincia)
                if Repositorio.fetchDataByNames('localidad', datoLocalidad['nombre']) == []:
                    Repositorio.insertData('localidad', datoLocalidad)
                if Repositorio.fetchDataByNameAndAddress(datoCentro['nombre'], datoCentro['direccion']) == []:
                    datoCentro['id_localidad'] = Repositorio.fetchDataByNames('localidad', datoLocalidad['nombre'])[0]['id']
                    Repositorio.insertData('centro_educativo', datoCentro)
                    resultado['correctos'] += 1
            else:
                resultado['rechazados'].append(error + datoCentro['nombre'] + ', ' + datoLocalidad['nombre'] + ', ' + motivo)

    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
    # Aqui se envia la informacion sobre la subida al frontend
    return resultado     
#xml_a_json()
#json_a_BD()
