from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time


def getText(url):

    driver_options = Options()
    driver_options.add_argument("--headless")  
    driver_options.add_argument("--log-level=3")  # Silenciar logs de ChromeDriver
    driver_options.add_argument("--disable-logging")  # Desactivar logs generales (opcional)
    driver = webdriver.Edge(options=driver_options)
    driver.get(url)
    time.sleep(1)
    capText = driver.find_element(By.ID,'chapter-container')
    text = capText.text 
    return text