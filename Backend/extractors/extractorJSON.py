import json
import os
import re
import sys 

ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)

from repositorio import *

def json_a_json():
    datos = []
    inserta = True
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/MUR.json'
    rutaNuevo = 'jsonResultFromWrapper/MUR_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))
    

    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        for fila in lector_json:
            inserta = True
            # Renombrar claves si existen
            if 'dencen' in fila:
                fila['nombre'] = fila.pop('dencen')
            else:
                inserta = False
                print('No existe la clave dencen')
                print(fila)

            if 'tipo' in fila:
                if 'concertad' in fila['presentacionCorta'].lower() or fila['denLarga'].lower() or fila['tipo'].lower():
                    fila['tipo'] = 'Concertado'
                else:
                    if 'privado' in fila['tipo'].lower():
                        fila['tipo'] = 'Privado'
                    if 'público' in fila['tipo'].lower():
                        fila['tipo'] = 'Público'
                    else:
                        print(fila['tipo'])
                        fila['tipo'] = 'Otros'

            if 'domcen' in fila:
                fila['direccion'] = fila.pop('domcen')
            else:
                inserta = False
                print('No existe la dirección')
                print(fila)
                
            if 'cpcen' in fila:
                fila['codigo_postal'] = fila.pop('cpcen')
                #cp = fila['cpcen']
                #fila['C_E.codigo_postal'] = str(cp).zfill(5) 
                #fila['LOC.codigo'] = str(cp).zfill(5)
                #fila['PRO.codigo'] = re.search(r'\d{2}', str(cp).zfill(5)).group()
            else:
                fila['codigo_postal'] = None
                print('No existe la clave cpcen')
                print(fila)
                
            if 'telcen' in fila:
                if len(fila['telcen']) == 9:
                    fila['telefono'] = fila.pop('telcen')
                else:
                    print('Número major o minor que 9 dígits')
                    fila['telefono'] = None
            else:
                if 'telcen2' in fila:
                    if len(fila['telcen2']) == 9:
                        fila['telefono'] = fila.pop('telcen2')
                    else:
                        print('Número major o minor que 9 dígits')
                        fila['telefono'] = None
                # print('No existe la clave telcen')
                else:
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
                if 'lat' in fila['geo-referencia']:
                    fila['latitud'] = fila['geo-referencia'].pop('lat')
                else:
                    fila['latitud'] = None
                    print('No existe la clave lat')
            else: 
                fila['longitud'] = None
                fila['latitud'] = None
                print('No existe la clave geo-referencia')
            #-----------------------------------------------------------------
                    
            if 'loccen' in fila:
                fila['localidad'] = fila.pop('loccen')
            else:
                print('No existe la clave loccen')
                print(fila)


            datoCentro = {
                'nombre': fila['nombre'],
                'tipo': fila['tipo'],
                'direccion': fila['direccion'],
                'codigo_postal': fila['codigo_postal'],
                'telefono': fila['telefono'],
                'descripcion': fila['descripcion'],
                'longitud': fila['longitud'],
                'latitud': fila['latitud'],
            }

            datoLocalidad = {
                'codigo': fila['codigo_postal'],
                'nombre': fila['localidad'],
                'en_provincia': 'Murcia'
            }

            #Repositorio.insertData('Centro_Educativo', datoCentro)
            
            #Repositorio.insertData('Localidad', datoLocalidad)



        datoProvincia = {
            'codigo': '30',
            'nombre': 'Murcia'        
        }

        Repositorio.insertData('Provincia', datoProvincia)


          
json_a_json()