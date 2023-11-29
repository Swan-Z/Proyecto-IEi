import csv
import json
import os

def Mapjson():
    # Lista para almacenar los datos del CSV
    datos = []
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/CV.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:
            if fila['REGIMEN'] == 'PRIV.':
                fila['Tipo']
            elif fila['REGIMEN'] == 'PÚB.':
                fila['Tipo'] = 'Publico'
            elif fila['REGIMEN'] == 'PRIV. CONC.':
                fila['Tipo'] = 'Concertado'
            else:
                fila['Tipo'] = 'Otros'

            datos.append(fila)

        for fila in lector_json:
            # Escribir los datos en formato JSON
            with open('jsonResultFromWrapper/nuevoArchivo.json', 'w') as archivoNuevo:
                json.dump(datos, archivoNuevo)
