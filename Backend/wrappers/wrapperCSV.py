import pandas as pd
import os

directorio_actual = os.getcwd()
rutaCSV = 'ficheroFuenteDatos/CV_DEF.csv'
rutaJSON = 'jsonResultFromWrapper/CV_DEF.json'
rutaComCSV = os.path.abspath(os.path.join(directorio_actual, rutaCSV))
rutaComJSON = os.path.abspath(os.path.join(directorio_actual, rutaJSON))

def wrapperCSV_to_JSON(pathCSV, pathJSON):
    csv = pd.read_csv(pathCSV, delimiter=';')
    jsonS = csv.to_json(orient='records', indent=2, force_ascii=False)
    
    jsonS = jsonS.replace('\/', '/')
    
    with open(pathJSON, 'w', encoding='utf-8') as json_file:
        json_file.write(jsonS)
    
wrapperCSV_to_JSON(rutaComCSV, rutaComJSON)