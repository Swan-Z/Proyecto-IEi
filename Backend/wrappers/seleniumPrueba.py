from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def verificar_titulo():
    driver = webdriver.Chrome()
    driver.get("https://www.coordenadas-gps.com/")
    # waiting = WebDriverWait(driver, 20)
    # waiting.until(EC.presence_of_element_located((By.ID, "latitude")))
   

    element = driver.find_element(By.ID,"address")
    element.send_keys("Universidad Politécnica de Valencia")
    element.submit()

    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'aswift_5')))
    driver.switch_to.frame(iframe)

    button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrap"]/div[2]/div[3]/div[1]/form[1]/div[2]/div/button')))
    button_element.click()
    

    print('Soy longitude:' + str(driver.find_element(By.ID, "longitude").get_attribute("value")))
    print('Soy latitude:' + str(driver.find_element(By.ID, "latitude").get_attribute("value")))


    driver.quit()

verificar_titulo()
    
        