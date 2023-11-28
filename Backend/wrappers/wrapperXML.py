import pandas as pd
import xmltodict
import os

#Los comentados es para probar directamente en este fichero
#python wrappers/fichero.py
# directorio_actual = os.getcwd()
# rutaXML = 'ficheroFuenteDatos/CAT.xml'
# rutaJSON = 'jsonResultFromWrapper/CAT.json'
# rutaComXML = os.path.abspath(os.path.join(directorio_actual, rutaXML))
# rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))

def XML_to_JSON(pathXML, pathJSON):
    with open(pathXML, 'rb') as file:
        xml_dict = xmltodict.parse(file)
        row = xml_dict['response']['row']

    df = pd.DataFrame(row)

    df.to_json(pathJSON, orient='records', indent=2)
    
# XML_to_JSON(rutaComXML, rutaComJSON)