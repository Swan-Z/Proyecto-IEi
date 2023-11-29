"""
Descripción del propósito de tu script.
Puedes añadir más detalles aquí si es necesario.
"""
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class seleniumExample:

    def VerificarTitulo(self):
        
        driver_path = 'path/to/chromedriver'
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("https://www.coordenadas-gps.com/")
        element = driver.find_element("id","address")
        element.send_Keys("Universidad Politécnica de Valencia")
        element.submit();

        # Aquí usamos Keys.ENTER para simular la tecla Enter
        element.send_keys(Keys.ENTER)

        # Use WebDriverWaait to wait for the presence of the element with id
        waiting = WebDriverWait(driver, 9)
        waiting.until(EC.presence_of_element_located((By.ID, "address")))
        
        # Check if the title matches the expected title
        if driver.title == "Universidad Politécnica de Valencia-Buscar con Google":
            print("PASA")
        else:
            print("FALLA")
        
        driver.quit()

# Instantiate the class and call the VerificarTitulo method
selenium_example = SeleniumExample()
selenium_example.VerificarTitulo()
