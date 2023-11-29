import json

def json_a_json(archivo_fuente):
    # Lista para almacenar los datos del JSON
    datos = []

    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(archivo_fuente, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        for fila in lector_json:

            # Renombrar claves si existen
            if 'dencen' in fila:
                fila['nombre'] = fila.pop('dencen')
            else:
                print('No existe la clave dencen')
                print(fila)
            if 'domcen' in fila:
                fila['direccion'] = fila.pop('domcen')
            else:
                print('No existe la clave domcen')
                print(fila)
            if 'cpcen' in fila:
                fila['codigo_postal'] = fila.pop('cpcen')
            else:
                print('No existe la clave cpcen')
                print(fila)
            if 'telcen' in fila:
                fila['telefono'] = fila.pop('telcen')
            else:
                print('No existe la clave telcen')
                print(fila)
            if 'presentacionCorta' in fila:
                fila['descripcion'] = fila.pop('presentacionCorta')
            else:
                print('No existe la clave presentacionCorta')
                print(fila)

            # Mover datos de georeferencia si existen
            if 'geo-referencia' in fila:
                if 'lon' in fila['geo-referencia']:
                    fila['longitud'] = fila['geo-referencia'].pop('lon')
                else:
                    print('No existe la clave lon')
                    print(fila)
                if 'lat' in fila['geo-referencia']:
                    fila['latitud'] = fila['geo-referencia'].pop('lat')
                else:
                    print('No existe la clave lat')
                    print(fila)

            datos.append(fila)

    print(datos[0])

json_a_json('C:/Users/pepep/Desktop/IEI/Proyecto-IEi/Backend/jsonResultFromWrapper/MUR.json')