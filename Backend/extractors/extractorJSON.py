import json
import os
import re
import sys 
import logging

ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)
logging.basicConfig(level=logging.WARNING)


class Colores:
    RESET = '\033[0m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'

from repositorio import *


def json_a_BD():
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/MUR_demo.json'
    # rutaNuevo = 'jsonResultFromWrapper/MUR_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    # rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))

    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        for fila in lector_json:
            # Renombrar claves si existen
            if 'dencen' in fila and fila['dencen'] is not None and fila['dencen'] != '':
                fila['nombre'] = fila.pop('dencen')
            else:  
                fila['nombre'] = None
                print(Colores.ROJO + 'No existe la clave dencen, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)

            if 'tipo' in fila:
                if 'concertad' in fila['presentacionCorta'].lower() or 'concertad' in fila['denLarga'].lower() or 'concertad' in fila['tipo'].lower():
                    fila['tipo'] = 'Concertado'
                else:
                    if 'privado' in fila['tipo'].lower():
                        fila['tipo'] = 'Privado'
                    elif 'público' in fila['tipo'].lower():
                        fila['tipo'] = 'Público'
                    else:
                        print(Colores.AMARILLO + 'No se ha podido determinar el tipo de centro: ' + Colores.RESET)
                        print(Colores.AMARILLO + str(fila) + Colores.RESET)
                        fila['tipo'] = 'Otros'
            else:
                fila['tipo'] = 'Otros'
                print(Colores.AMARILLO + 'No existe la clave tipo: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)
            if 'domcen' in fila and fila['domcen'] is not None and fila['domcen'] != '':
                fila['direccion'] = fila.pop('domcen')
            else:
                fila['direccion'] = None
                print(Colores.ROJO + 'No existe la dirección, por lo tanto esta fila no será insertada: '+ Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                
            if 'cpcen' in fila and fila['cpcen'] is not None and fila['cpcen'] != '':
                fila['codigo_postal'] = fila.pop('cpcen')
            else:
                fila['codigo_postal'] = None
                print(Colores.ROJO + 'No existe la clave cpcen, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                
            if 'telcen' in fila:
                if len(fila['telcen']) == 9:
                    fila['telefono'] = fila.pop('telcen')
                else:
                    print(Colores.AMARILLO +'Número con formato erroneo: ' + Colores.RESET)
                    print(Colores.AMARILLO + str(fila) + Colores.RESET)
                    fila['telefono'] = None
            else:
                if 'telcen2' in fila:
                    if len(fila['telcen2']) == 9:
                        fila['telefono'] = fila.pop('telcen2')
                    else:
                        print(Colores.AMARILLO +'Número con formato erroneo: ' + Colores.RESET)
                        print(Colores.AMARILLO + str(fila) + Colores.RESET)
                        fila['telefono'] = None
                else:
                    print(Colores.AMARILLO + 'No existe la clave telcen: ' + Colores.RESET)
                    print(Colores.AMARILLO + str(fila) + Colores.RESET)
                    fila['telefono'] = None
                
            if 'presentacionCorta' in fila:
                fila['descripcion'] = fila.pop('presentacionCorta')
            else:
                fila['descripcion'] = None
                print(Colores.AMARILLO + 'No existe la clave presentacionCorta: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)

            # Mover datos de georeferencia si existen
            if 'geo-referencia' in fila:
                if 'lon' in fila['geo-referencia'] and fila['geo-referencia']['lon'] is not None and fila['geo-referencia']['lon'] != '':
                    fila['longitud'] = fila['geo-referencia'].pop('lon')
                else:
                    fila['lon'] = None
                    print(Colores.ROJO + 'No existe la clave lon por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
                if 'lat' in fila['geo-referencia'] and fila['geo-referencia']['lat'] is not None and fila['geo-referencia']['lat'] != '':
                    fila['latitud'] = fila['geo-referencia'].pop('lat')
                else:
                    fila['latitud'] = None
                    print(Colores.ROJO + 'No existe la clave lat por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
            else: 
                fila['longitud'] = None
                fila['latitud'] = None
                print(Colores.ROJO + 'No existe la clave geo-referencia, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
            #-----------------------------------------------------------------
                    
            if 'loccen' in fila and fila['loccen'] is not None and fila['loccen'] != '':
                fila['localidad'] = fila.pop('loccen')
            else:
                print(Colores.ROJO + 'No existe la clave loccen, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                fila['localidad'] = None

            datoCentro = {
                'nombre': fila['nombre'],
                'tipo': fila['tipo'],
                'direccion': fila['direccion'],
                'codigo_postal': fila['codigo_postal'],
                'telefono': fila['telefono'],
                'descripcion': fila['descripcion'],
                'longitud': fila['longitud'],
                'latitud': fila['latitud'],   
                'id_localidad' : ''            
            }

            datoLocalidad = {
                'nombre': fila['localidad'],
                'en_provincia': 'Murcia'
            }

            if datoCentro['nombre'] and datoCentro['direccion'] and datoCentro['longitud'] and datoCentro['latitud'] and datoCentro['codigo_postal']:            
                Repositorio.insertData('Localidad', datoLocalidad)
                datoCentro['id_localidad'] = Repositorio.fetchDataByNames('Localidad', datoLocalidad['nombre'])[0]['id']
                Repositorio.insertData('Centro_Educativo', datoCentro)
            else:
                print('')
                


def insertaProvincia():
    datoProvincia = {
        'codigo': '30',
        'nombre': 'Murcia'
    }
    Repositorio.insertData('Provincia', datoProvincia)

insertaProvincia()      
json_a_BD()