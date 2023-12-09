import json
import os
import re
import sys 

ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)

from repositorio import *

class SequentialIDGenerator:
    def __init__(self):
        self.counter = 0

    def generate_id(self):
        self.counter += 1
        return self.counter

def json_a_BD():
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/MUR.json'
    # rutaNuevo = 'jsonResultFromWrapper/MUR_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    # rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))
    generator = SequentialIDGenerator()

    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        for fila in lector_json:
            # Renombrar claves si existen
            if 'dencen' in fila:
                fila['nombre'] = fila.pop('dencen')
            else:  
                fila['nombre'] = None
                print('No existe la clave dencen, por lo tanto esta fila no será insertada')
                print(fila)

            if 'tipo' in fila:
                if 'concertad' in fila['presentacionCorta'].lower() or 'concertad' in fila['denLarga'].lower() or 'concertad' in fila['tipo'].lower():
                    fila['tipo'] = 'Concertado'
                else:
                    if 'privado' in fila['tipo'].lower():
                        fila['tipo'] = 'Privado'
                    elif 'público' in fila['tipo'].lower():
                        fila['tipo'] = 'Público'
                    else:
                        print('No se ha podido determinar el tipo de centro')
                        print(fila)
                        fila['tipo'] = 'Otros'
            else:
                fila['tipo'] = 'Otros'
                print('No existe la clave tipo')
                print(fila)
            if 'domcen' in fila:
                fila['direccion'] = fila.pop('domcen')
            else:
                fila['direccion'] = None
                print('No existe la dirección, por lo tanto esta fila no será insertada')
                print(fila)
                
            if 'cpcen' in fila:
                fila['codigo_postal'] = fila.pop('cpcen')
            else:
                fila['codigo_postal'] = None
                print('No existe la clave cpcen')
                print(fila)
                
            if 'telcen' in fila:
                if len(fila['telcen']) == 9:
                    fila['telefono'] = fila.pop('telcen')
                else:
                    print('Número con formato erroneo')
                    print(fila)
                    fila['telefono'] = None
            else:
                if 'telcen2' in fila:
                    if len(fila['telcen2']) == 9:
                        fila['telefono'] = fila.pop('telcen2')
                    else:
                        print('Número con formato erroneo')
                        fila['telefono'] = None
                else:
                    print('No existe la clave telcen')
                    print(fila)
                    fila['telefono'] = None
                
            if 'presentacionCorta' in fila:
                fila['descripcion'] = fila.pop('presentacionCorta')
            else:
                fila['descripcion'] = None
                print('No existe la clave presentacionCorta')
                print(fila)

            # Mover datos de georeferencia si existen
            if 'geo-referencia' in fila:
                if 'lon' in fila['geo-referencia']:
                    fila['longitud'] = fila['geo-referencia'].pop('lon')
                else:
                    fila['lon'] = None
                    print('No existe la clave lon')
                    print(fila)
                if 'lat' in fila['geo-referencia']:
                    fila['latitud'] = fila['geo-referencia'].pop('lat')
                else:
                    fila['latitud'] = None
                    print('No existe la clave lat')
                    print(fila)
            else: 
                fila['longitud'] = None
                fila['latitud'] = None
                print('No existe la clave geo-referencia')
                print(fila)
            #-----------------------------------------------------------------
                    
            if 'loccen' in fila:
                fila['localidad'] = fila.pop('loccen')
            else:
                print('No existe la clave loccen')
                print(fila)
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

            if datoCentro['nombre'] != None and datoCentro['direccion'] != None:
                Repositorio.insertData('Localidad', datoLocalidad)
                datoCentro['id_localidad'] = Repositorio.fetchDataByNames('Localidad', datoLocalidad['nombre'])[0]['id']
                Repositorio.insertData('Centro_Educativo', datoCentro)
            else:
                print(fila)
                print('No ha insertado esta fila porque contiene atributos nulos que no pueden ser nulos')


def insertaProvincia():
    datoProvincia = {
        'codigo': '30',
        'nombre': 'Murcia'
    }
    Repositorio.insertData('Provincia', datoProvincia)

insertaProvincia()      
json_a_BD()