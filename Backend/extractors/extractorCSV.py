import csv
import json

def csv_a_json(archivo_csv, archivo_json):
    # Lista para almacenar los datos del CSV
    datos = []

    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')
        for fila in lector_csv:
            if fila['REGIMEN'] == 'PRIV.':
                fila['Tipo'] = 'Privado'
            elif fila['REGIMEN'] == 'PÚB.':
                fila['Tipo'] = 'Publico'
            elif fila['REGIMEN'] == 'PRIV. CONC.':
                fila['Tipo'] = 'Concertado'
            else:
                fila['Tipo'] = 'Otros'

            datos.append(fila)

        for fila in lector_csv:
            # Escribir los datos en formato JSON
            with open(archivo_json, 'w') as archivo:
                json.dump(datos, archivo, indent=2)
