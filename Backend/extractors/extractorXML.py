import json
import os
import re  

def xml_a_json():
    datos = []
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/CAT.json'
    rutaNuevo = 'jsonResultFromWrapper/CAT_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))
    

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:

            

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

xml_a_json()
