import csv
import json

def csv_a_json(archivo_csv, archivo_json):
    # Lista para almacenar los datos del CSV
    datos = []

    # Abrir el archivo CSV y leer los datos con la codificación 'utf-8'
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')
        for fila in lector_csv:
            fila['COD'] = fila.pop('CODIGO')
            datos.append(fila)

    # Escribir los datos en formato JSON
    with open(archivo_json, 'w') as archivo:
        json.dump(datos, archivo, indent=2)
