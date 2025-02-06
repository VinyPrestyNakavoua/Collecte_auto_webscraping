# Récupérez sur le site www. la-maronne-immobiliere. com l’ensemble des informations standard sur les
# biens immobiliers situés à moins de 50 km d’Aurillac.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# on va recuoperer des informations standars sur ce site, sachant que c'est un site dynamique

# On crée un simulateur de navigateur web, ici Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# On connecte le simulateur à Google
driver.get("https://www.la-maronne-immobiliere.com/")


# on ne va pas chercher à cliquer sur le bouton des cookies, parce que ça devient un peu compliqué

# On patiente quelques secondes que la page se charge entièrement
sleep(3)

# on va faire un try except pour que s'il n'arrive pas à cliquer sur le boutton

try:
    cookiebutton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".cookieBtn.green")))

    driver.execute_script("arguments[0].click();", cookiebutton)    # on va utiliser execute_script pour forcer le click avec js

except TimeoutException:

    # On détecte le bouton "Accepter les cookies"
    buttonclose = driver.find_element(By.CLASS_NAME, "close")

    # On clique sur ce bouton
    buttonclose.click()


# on va maintenant entrer les elements dans la barre de filtre puis cliquer sur le bouton recherche

# entrer la ville
ville = driver.find_element(By.CSS_SELECTOR, ".input_text.city_autocomplete.ui-autocomplete-input")
ville.send_keys("Aurillac,")
ville.send_keys("Aurillac 15000,")


# cliquer sur recherche

sleep(3)

recherchebutton = driver.find_element(By.CSS_SELECTOR, ".btn.search")

recherchebutton.click()

sleep(5)

# laisser du temps à la page pour bien se charger

# nous voila sur la nouvelle page

# ensuite il faut entrer la distance autour d'aurillac
# la div : search_block search_radius search_title
div = driver.find_element(By.CSS_SELECTOR, ".search_block search_radius.search_title")
dropdown_button = div.find_element(By.CSS_SELECTOR, ".ui-multiselect.ui-widget.ui-state-default.ui-corner-all")
dropdown_button.click()


# un petit sleep
sleep(3)


# cliquer sur le bouton recherche : 
recherchebutton = driver.find_element(By.CSS_SELECTOR, ".btn.search")

recherchebutton.click()

# collecte des données

result_req = driver.find_element(By.ID, "result")

# getting elemnts
div_req = result_req.find_elements(By.CLASS_NAME, "res_div1")

print(div_req)










