import json
import os
import re  

def csv_a_json():
    datos = []
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/CV.json'
    rutaNuevo = 'jsonResultFromWrapper/CV_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))
    

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:

            if 'DENOMINACION_GENERICA_ES' in fila:
                fila['C_E.nombre'] = fila.pop('DENOMINACION_GENERICA_ES')
            else:
                print('No existe la clave DENOMINACION_GENERICA_ES')
                print(fila)
            
            if 'REGIMEN' in fila:
                if fila['REGIMEN'] == 'PRIV.':
                    fila['C_E.tipo'] = 'privado'
                elif fila['REGIMEN'] == 'PÚB.':
                    fila['C_E.tipo'] = 'Publico'
                elif fila['REGIMEN'] == 'PRIV. CONC.':
                    fila['C_E.tipo'] = 'Concertado'
                elif fila['REGIMEN'] == 'OTROS':
                    fila['C_E.tipo'] = 'Otros'
                fila.pop('REGIMEN')
            else:
                print('No detecta el REGIMEN')
                print(fila) 
            
            if 'TIPO_VIA' or 'DIRECCION' or 'NUMERO' in fila:
                fila['C_E.direccion'] = str(fila.pop('TIPO_VIA')) + ", " + str(fila.pop('DIRECCION')) + ", " + str(fila.pop('NUMERO'))
            else:
                print('No existe la clave TIPO_VIA o DIRECCION o NUMERO')
                print(fila)
            if 'CODIGO_POSTAL' in fila:
                cp = fila['CODIGO_POSTAL']
                fila['C_E.codigo_postal'] = cp
                fila['Log.codigo'] = cp
                str(cp).zfill(5)
                fila['Pro.codigo'] = int(re.search(r'\d{2}', str(cp)).group())
                fila.pop('CODIGO_POSTAL')
            else:
                print('No existe la clave CODIGO_POSTAL')
                print(fila)
            if 'TELEFONO' in fila:
                fila['C_E.telefono'] = fila.pop('TELEFONO')
            else:
                print('No existe la clave TELEFONO')
                print(fila)
            if 'URL_ES' in fila:
                fila['C_E.descripcion'] = fila.pop('URL_ES')
            else:
                print('No existe la clave URL_ES')
                print(fila)
            if 'LOCALIDAD' in fila:
                fila['Log.nombre'] = fila.pop('LOCALIDAD')
            else:
                print('No existe la clave LOCALIDAD')
                print(fila)
            if 'PROVINCIA' in fila:
                fila['Pro.nombre'] = fila.pop('PROVINCIA')
            else:
                print('No existe la clave PROVINCIA')
                print(fila)

            nuevo_dato = {
                'C_E.nombre': fila['C_E.nombre'],
                'C_E.tipo': fila['C_E.tipo'],
                'C_E.direccion': fila['C_E.direccion'],
                'C_E.codigo_postal': fila['C_E.codigo_postal'],
                'C_E.telefono': fila['C_E.telefono'],
                'C_E.descripcion': fila['C_E.descripcion'],
                'Log.nombre': fila['Log.nombre'],
                'Log.codigo': fila['Log.codigo'],
                'Pro.nombre': fila['Pro.nombre'],
                'Pro.codigo': fila['Pro.codigo']
            }
            datos.append(nuevo_dato)
        
        with open(rutaComNuevo, 'w', encoding='utf-8') as archivoNuevo:
            json.dump(datos, archivoNuevo, indent=2, ensure_ascii=False)

csv_a_json()
