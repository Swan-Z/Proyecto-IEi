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

    resultado = {
         'correctos': 0,
         'reparados': [],
         'rechazados': [],
    }

    datoProvincia = {
        'codigo': '30',
        'nombre': 'Murcia'
    }
    Repositorio.insertData('provincia', datoProvincia)

    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        # En este for se recorre cada fila del JSON y se van incorporando las filas a la base de datos como corresponde, 
        # tambien se gestionan los errores que puedan surgir
        for fila in lector_json:
            reparado=False
            rechazado=False
            error = 'Murcia, '
            motivo = ''
            arreglo = ''
            # Aqui se recupera el valor de la clave dencen y se le asigna a la clave nombre
            if 'dencen' in fila and fila['dencen'] is not None and fila['dencen'] != '':
                fila['nombre'] = fila.pop('dencen')
            else:  
                fila['nombre'] = ''
                print(Colores.ROJO + 'No existe la clave dencen, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                rechazado=True
                motivo += 'no tiene nombre. '
            # Aqui se recupera el valor de la clave titularidad y se le asigna a la clave tipo
            if 'titularidad' in fila:
                if 'C' in fila['titularidad']:
                    fila['tipo'] = 'Concertado'
                else:
                    if 'N' in fila['titularidad']:
                        fila['tipo'] = 'Privado'
                    elif 'P' in fila['titularidad']:
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
                print(Colores.AMARILLO + 'No existe la clave tipo: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)
                reparado=True
                motivo += 'no se ha podido determinar el tipo de centro, '
                arreglo += 'se le ha asignado el tipo Otros, '
            # Aqui se recupera el valor de la clave domcen y se le asigna a la clave direccion
            if 'domcen' in fila and fila['domcen'] is not None and fila['domcen'] != '':
                fila['direccion'] = fila.pop('domcen')
            else:
                fila['direccion'] = ''
                print(Colores.ROJO + 'No existe la dirección, por lo tanto esta fila no será insertada: '+ Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                rechazado=True
                motivo += 'no tiene dirección. '
            # Aqui se recupera el valor de la clave cpcen y se le asigna a la clave codigo_postal
            if 'cpcen' in fila and fila['cpcen'] is not None and fila['cpcen'] != '':
                fila['codigo_postal'] = fila.pop('cpcen')
            else:
                fila['codigo_postal'] = ''
                print(Colores.ROJO + 'No existe la clave cpcen, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                rechazado=True
                motivo += 'no tiene código postal. '
            # Aqui se recupera el valor de la clave telcen y se le asigna a la clave telefono
            if 'telcen' in fila:
                if len(fila['telcen']) == 9:
                    fila['telefono'] = fila.pop('telcen')
                else:
                    print(Colores.AMARILLO +'Número con formato erroneo: ' + Colores.RESET)
                    print(Colores.AMARILLO + str(fila) + Colores.RESET)
                    fila['telefono'] = None
                    reparado=True
                    motivo += 'número con formato erroneo, '
                    arreglo += 'se ha dejado el campo del teléfono vacío.'
            else:
                if 'telcen2' in fila:
                    if len(fila['telcen2']) == 9:
                        fila['telefono'] = fila.pop('telcen2')
                    else:
                        print(Colores.AMARILLO +'Número con formato erroneo: ' + Colores.RESET)
                        print(Colores.AMARILLO + str(fila) + Colores.RESET)
                        fila['telefono'] = None
                        reparado=True
                        motivo += 'número con formato erroneo, '
                        arreglo += 'se ha dejado el campo del teléfono vacío, '
                else:
                    print(Colores.AMARILLO + 'No existe la clave telcen: ' + Colores.RESET)
                    print(Colores.AMARILLO + str(fila) + Colores.RESET)
                    fila['telefono'] = None
                    reparado=True
                    motivo += 'no tiene teléfono, '
                    arreglo += 'se ha dejado el campo del teléfono vacío, '
            # Aqui se recupera el valor de la clave presentacionCorta y se le asigna a la clave descripcion
            if 'presentacionCorta' in fila:
                fila['descripcion'] = fila.pop('presentacionCorta')
            else:
                fila['descripcion'] = None
                print(Colores.AMARILLO + 'No existe la clave presentacionCorta: ' + Colores.RESET)
                print(Colores.AMARILLO + str(fila) + Colores.RESET)

            # Mover datos de georeferencia si existen
            if 'geo-referencia' in fila:
                # Aqui se recupera el valor de la clave lon y se le asigna a la clave longitud
                if 'lon' in fila['geo-referencia'] and fila['geo-referencia']['lon'] is not None and fila['geo-referencia']['lon'] != '':
                    fila['longitud'] = fila['geo-referencia'].pop('lon')
                else:
                    fila['lon'] = None
                    print(Colores.ROJO + 'No existe la clave lon por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
                    rechazado=True
                    motivo += 'no tiene longitud. '
                # Aqui se recupera el valor de la clave lat y se le asigna a la clave latitud
                if 'lat' in fila['geo-referencia'] and fila['geo-referencia']['lat'] is not None and fila['geo-referencia']['lat'] != '':
                    fila['latitud'] = fila['geo-referencia'].pop('lat')
                else:
                    fila['latitud'] = None
                    print(Colores.ROJO + 'No existe la clave lat por lo tanto esta fila no será insertada: ' + Colores.RESET)
                    print(Colores.ROJO + str(fila) + Colores.RESET)
                    rechazado=True
                    motivo += 'no tiene latitud. '
            else: 
                fila['longitud'] = None
                fila['latitud'] = None
                print(Colores.ROJO + 'No existe la clave geo-referencia, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                rechazado=True
                motivo += 'no tiene longitud ni latitud. '
            #-----------------------------------------------------------------
            # Aqui se recupera el valor de la clave loccen y se le asigna a la clave localidad   
            if 'loccen' in fila and fila['loccen'] is not None and fila['loccen'] != '':
                fila['localidad'] = fila.pop('loccen')
            else:
                print(Colores.ROJO + 'No existe la clave loccen, por lo tanto esta fila no será insertada: ' + Colores.RESET)
                print(Colores.ROJO + str(fila) + Colores.RESET)
                fila['localidad'] = ''
                rechazado=True
                motivo += 'no tiene localidad. '

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
            # Aqui se comprueba si la fila ha sido rechazada
            if not rechazado:
                # Aqui se comprueba si la fila ha sido reparada, y se inserta el string correspondiente del aviso de esto, y 
                # se comprueban tambien que no esten ya en la base de datos los datos que se van a insertar
                if reparado:
                    resultado['reparados'].append(error + datoCentro['nombre'] + ', ' + datoLocalidad['nombre'] + ', ' + motivo + arreglo)
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
json_a_BD()