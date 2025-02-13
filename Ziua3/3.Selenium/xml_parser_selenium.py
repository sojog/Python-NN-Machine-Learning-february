from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

try:
    # Inițializăm driverul Chrome
    driver = webdriver.Chrome()
    
    # Deschidem fișierul XML local
    driver.get("file:///" + os.path.abspath("fisier.xml"))
    
    # Așteptăm să se încarce pagina și găsim toate elementele deployment
    wait = WebDriverWait(driver, 10)
    deployments = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//deployment"))
    )
    
    # Extragem și afișăm numele deployment-urilor
    print("Deployment-uri găsite:")
    for deployment in deployments:
        name = deployment.get_attribute("name")
        if name:
            print(f"- {name}")
            
except Exception as e:
    print(f"A apărut o eroare: {e}")
finally:
    # Închidem browser-ul
    try:
        driver.quit()
    except:
        pass