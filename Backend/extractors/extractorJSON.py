import json

def json_a_json(archivo_fuente,archivo_destino):
    # Lista para almacenar los datos del JSON
    datos = []

    # Abrir el archivo JSON y leer los datos con la codificación 'utf-8'
    with open(archivo_fuente, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)
        for fila in lector_json:
            fila['nombre'] = fila.pop('dencen')
            fila['direccion'] = fila.pop('domcen')
            fila['codigo_postal'] = fila.pop('cpcen')
            fila['longitud'] = fila.pop('geo-referencia'['lon']) 
            fila['latitud'] = fila.pop('geo-referencia'['lat']) 
            #fila['direccion'] = fila.pop('domcen')


            datos.append(fila)

    # Escribir los datos en formato JSON
    with open(archivo_destino, 'w') as archivo:
        json.dump(datos, archivo, indent=2)
    