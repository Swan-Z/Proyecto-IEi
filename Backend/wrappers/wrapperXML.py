import pandas as pd
import xmltodict
import os

#Los comentados es para probar directamente en este fichero
#python wrappers/fichero.py
# directorio_actual = os.getcwd()
# rutaXML = 'ficheroFuenteDatos/CAT_demo.xml'
# rutaJSON = 'jsonResultFromWrapper/CAT_demo.json'
# rutaComXML = os.path.abspath(os.path.join(directorio_actual, rutaXML))
# rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))

def wrapperXML_to_JSON(pathXML, pathJSON):
    with open(pathXML, 'rb') as file:
        xml_dict = xmltodict.parse(file)
        row = xml_dict['response']['row']
    df = pd.DataFrame(row)
    df = df.to_json(orient='records', indent=2, force_ascii=False)
    df = df.replace('\/', '/')
    
    with open(pathJSON, 'w', encoding='utf8') as file:
        file.write(df)
    
    
    
# wrapperXML_to_JSON(rutaComXML, rutaComJSON)