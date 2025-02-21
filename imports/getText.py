from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time


def getText(url):

    driver_options = Options()
    driver_options.add_argument("--headless=new")  
    driver_options.add_argument("--log-level=3")  # Silenciar logs de ChromeDriver
    driver_options.add_argument("--disable-logging")  # Desactivar logs generales (opcional)
    driver_options.add_argument("--disable-notifications")  # Desactivar notificaciones
    driver_options.add_argument("--disable-gpu") # Desactivar GPU
    driver_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=driver_options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.ID, "chapter-container")))
    capText = driver.find_element(By.ID,'chapter-container')
    text = capText.text 
    driver.quit()
    return text