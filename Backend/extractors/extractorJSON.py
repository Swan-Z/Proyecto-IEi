import json
import os
import re

def json_a_json():
    datos = []
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/MUR.json'
    rutaNuevo = 'jsonResultFromWrapper/MUR_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))

    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        for fila in lector_json:

            # Renombrar claves si existen
            if 'dencen' in fila:
                fila['C_E.nombre'] = fila.pop('dencen')
            else:
                print('No existe la clave dencen')
                print(fila)

            if 'tipo' in fila:
                if 'concertado' in fila['presentacionCorta']:
                    fila['C_E.tipo'] = 'concertado'
                elif 'Privado' in fila['tipo']:
                    fila['C_E.tipo'] = 'privado'
                elif 'Público' in fila['tipo']:
                    fila['C_E.tipo'] = 'publico'
                else:
                    fila['C_E.tipo'] = 'Otros'
            else:
                print('No detecta el REGIMEN')
                print(fila) 
            if 'domcen' in fila:
                fila['C_E.direccion'] = fila.pop('domcen')
            else:
                print('No existe la clave domcen')
                print(fila)
            if 'cpcen' in fila:
                cp = fila['cpcen']
                fila['C_E.codigo_postal'] = str(cp).zfill(5) 
                fila['LOC.codigo'] = str(cp).zfill(5)
                fila['PRO.codigo'] = re.search(r'\d{2}', str(cp).zfill(5)).group()
            else:
                print('No existe la clave cpcen')
                print(fila)
            if 'telcen' in fila:
                fila['C_E.telefono'] = fila.pop('telcen')
            else:
                # print('No existe la clave telcen')
                # print(fila)
                fila['C_E.telefono'] = None
            if 'presentacionCorta' in fila:
                fila['C_E.descripcion'] = fila.pop('presentacionCorta')
            else:
                print('No existe la clave presentacionCorta')
                print(fila)

            # Mover datos de georeferencia si existen
            if 'geo-referencia' in fila:
                if 'lon' in fila['geo-referencia']:
                    fila['C_E.longitud'] = fila['geo-referencia'].pop('lon')
                else:
                    print('No existe la clave lon')
                    print(fila)
                if 'lat' in fila['geo-referencia']:
                    fila['C_E.latitud'] = fila['geo-referencia'].pop('lat')
                else:
                    print('No existe la clave lat')
                    print(fila)
            if 'loccen' in fila:
                fila['LOC.nombre'] = fila.pop('loccen')
            else:
                print('No existe la clave loccen')
                print(fila)
            if 'muncen' in fila:
                fila['PRO.nombre'] = fila.pop('muncen')
            else:
                print('No existe la clave muncen')
                print(fila)

            nuevo_dato = {
                'C_E.nombre': fila['C_E.nombre'],
                'C_E.tipo': fila['C_E.tipo'],
                'C_E.direccion': fila['C_E.direccion'],
                'C_E.codigo_postal': fila['C_E.codigo_postal'],
                'C_E.telefono': fila['C_E.telefono'],
                'C_E.descripcion': fila['C_E.descripcion'],
                'LOC.nombre': fila['LOC.nombre'],
                'LOC.codigo': fila['LOC.codigo'],
                'PRO.nombre': fila['PRO.nombre'],
                'PRO.codigo': fila['PRO.codigo']
            }
            datos.append(nuevo_dato)

        with open(rutaComNuevo, 'w', encoding='utf-8') as archivoNuevo:
            json.dump(datos, archivoNuevo, indent=2, ensure_ascii=False)

json_a_json()