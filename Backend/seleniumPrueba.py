"""
Descripción del propósito de tu script.
Puedes añadir más detalles aquí si es necesario.
"""
import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from repositorio import *


ruta_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_backend)

def inicializar_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.coordenadas-gps.com/")
    return driver

def verificar_titulo(direccion, driver):
    """
    Verifica el título de la página después de realizar una búsqueda.
    Args: direccion (str): La dirección que se utilizará para la búsqueda.
    Returns: dict: Un diccionario que contiene las coordenadas geográficas (latitud y longitud).
    """
    #driver_path = 'path/to/chromedriver'
    # para que no se cierre la página
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=option)
    
    # para que se cierre automaticamente después de ejecutar(quita la option en Chrome())
    # waiting = WebDriverWait(driver, 20)
    # waiting.until(EC.presence_of_element_located((By.ID, "latitude")))

    element = driver.find_element(By.ID,"address")
    element.clear()
    element.send_keys(direccion)
    #element.submit()

    # Hacer clic en el botón "Obtener Coordenadas GPS"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Obtener Coordenadas GPS']")))
    button.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "longitude")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "latitude")))
    
    time.sleep(5) #para que la página se carga las informaciones, depende de la velocidad de recargar

    longitude_element = driver.find_element(By.ID, "longitude")
    latitude_element = driver.find_element(By.ID, "latitude")

    res1 = longitude_element.get_attribute("value")
    res2 = latitude_element.get_attribute("value")

    dato_geo = {
        'longitud': res1,
        'latitud': res2
    }

    # print('Soy latitude:' + res2)
    # print('Soy longitude:' + res1)
    
    #driver.quit()
    return dato_geo
    

    


    
        