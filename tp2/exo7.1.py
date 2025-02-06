


# Récupérez sur le site www. la-maronne-immobiliere. com l’ensemble des informations standard sur les
# biens immobiliers situés à moins de 50 km d’Aurillac.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


# on va recuoperer des informations standars sur ce site, sachant que c'est un site dynamique

# On crée un simulateur de navigateur web, ici Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# On connecte le simulateur à Google
driver.get("https://www.la-maronne-immobiliere.com/")

# bouton cookie

cookiebutton = driver.find_element(By.CSS_SELECTOR, ".cookieBtn.green")

print(cookiebutton)

# cliquer sur le bouton
cookiebutton.click()

# On patiente quelques secondes que la page se charge entièrement
sleep(60)









