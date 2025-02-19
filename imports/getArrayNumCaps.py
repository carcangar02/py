from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time


def getArrayNumCaps(urlCap,numCap):

    driver_options = Options()
    driver_options.add_argument("--headless")  
    driver_options.add_argument("--log-level=3")  # Silenciar logs de ChromeDriver
    driver_options.add_argument("--disable-logging")  # Desactivar logs generales (opcional)
    driver = webdriver.Edge(options=driver_options)
    driver.get(urlCap)
    
    time.sleep(1)
    seccionTitulo = driver.find_element(By.TAG_NAME, 'h1')
    enlaceContenerdor = seccionTitulo.find_element(By.CLASS_NAME, 'booktitle')
    enlace = enlaceContenerdor.get_attribute('href')
    driver.get(enlace)
    time.sleep(1)
    elemento_padre = driver.find_element(By.CLASS_NAME, "header-stats")

    # Encontrar el primer <span> dentro del elemento padre
    primer_span = elemento_padre.find_element(By.TAG_NAME, "span")

    # Encontrar el <strong> dentro del primer <span>
    strong_element = primer_span.find_element(By.TAG_NAME, "strong")

    # Obtener el texto del <strong>
    numCapFinalstr = strong_element.text
    numCapFinal = int(numCapFinalstr)
    print(f'ultimo cap -> {numCapFinal}')
    arrayNumCaps = list(range(numCap,numCapFinal+1))
    return arrayNumCaps