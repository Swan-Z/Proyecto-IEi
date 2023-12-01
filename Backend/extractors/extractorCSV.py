import json
import os
import re  

def csv_a_json():
    datos = []
    insert = True
    directorio_actual = os.getcwd()
    rutaJSON = 'jsonResultFromWrapper/CV.json'
    rutaNuevo = 'jsonResultFromWrapper/CV_Nuevo.json'
    rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))
    rutaComNuevo = os.path.abspath(os.path.join(directorio_actual, rutaNuevo))

    

    with open(rutaComJSON, 'r', encoding='utf-8') as archivo:
        lector_json = json.load(archivo)

        for fila in lector_json:
            insert = True
            if 'DENOMINACION_GENERICA_ES' in fila:
                fila['nombre'] = fila.pop('DENOMINACION_GENERICA_ES')
            else:
                insert = False
                print('No existe la clave DENOMINACION_GENERICA_ES')
                print(fila)
            
            if 'REGIMEN' in fila:
                if fila['REGIMEN'] == 'PRIV.':
                    fila['tipo'] = 'privado'
                elif fila['REGIMEN'] == 'PÚB.':
                    fila['tipo'] = 'Publico'
                elif fila['REGIMEN'] == 'PRIV. CONC.':
                    fila['tipo'] = 'Concertado'
                elif fila['REGIMEN'] == 'OTROS':
                    fila['tipo'] = 'Otros'
            else:
                insert = False
                print('No detecta el tipo')
                print(fila) 
            
            if 'TIPO_VIA' or 'DIRECCION' or 'NUMERO' in fila:
                fila['direccion'] = str(fila.pop('TIPO_VIA')) + ", " + str(fila.pop('DIRECCION')) + ", " + str(fila.pop('NUMERO'))
            else:
                print('No existe la dirección')
                print(fila)
            if 'CODIGO_POSTAL' in fila:
                cp = fila['CODIGO_POSTAL']
                fila['codigo_postal'] = str(cp).zfill(5)  #añadir 0 por delante
                fila['LOC.codigo'] = str(cp).zfill(5)
                fila['PRO.codigo'] = re.search(r'\d{2}', str(cp).zfill(5)).group()
            else:
                fila['codigo_postal'] = None
                print('No existe la clave CODIGO_POSTAL')
                print(fila)
            if 'TELEFONO' in fila:
                if len(fila['TELEFONO']) == 9:
                    fila['telefono'] = fila.pop('TELEFONO')
                else:
                    print('Número mayor o menor que 9 dígitos')
                    fila['telefono'] = None
            else:
                print('No existe la clave TELEFONO')
                print(fila)
            if 'URL_ES' in fila:
                fila['descripcion'] = fila.pop('URL_ES')
            else:
                fila['descripcion'] = None
                print('No existe la clave URL_ES')
                print(fila)
            if 'LOCALIDAD' in fila:
                fila['LOC.nombre'] = fila.pop('LOCALIDAD')
            else:
                print('No existe la clave LOCALIDAD')
                print(fila)
            if 'PROVINCIA' in fila:
                fila['PRO.nombre'] = fila.pop('PROVINCIA')
            else:
                print('No existe la clave PROVINCIA')
                print(fila)

            datoCentro = {
                'nombre': fila['nombre'],
                'tipo': fila['tipo'],
                'direccion': fila['direccion'],
                'codigo_postal': fila['codigo_postal'],
                'telefono': fila['telefono'],
                'descripcion': fila['descripcion'],
            }

            datoLocalidad = {
                'codigo': fila['codigo_postal'],
                'nombre': fila['PRO.nombre']
            }

            datoProvincia = {
                'codigo': fila['codigo_postal'],
                'nombre': fila['PRO.nombre']          
            }
            datos.append(datoCentro)
        
        with open(rutaComNuevo, 'w', encoding='utf-8') as archivoNuevo:
            json.dump(datos, archivoNuevo, indent=2, ensure_ascii=False)

csv_a_json()
