# on a vu qu'on pouvait recupere les données des sites statistiques
# cette fois-ci on va utiliser selenium pour recuperer les données des sites dynamiques ceux contenant
# du javascript, et c'est ici qu'on va utiliser les xpath

# Xpath : c'est quoi
# XPath est un outil puissant pour localiser des éléments HTML de manière précise, 
# ce qui est essentiel en web scraping.
# Il fonctionne avec Selenium, Scrapy et BeautifulSoup.
# Il permet d’extraire, filtrer et manipuler facilement les données.
# en gros comme en css pour donner un style à un element
# si je veux donner color = 'bleu' a tous les titres h1, en css j'ecris jsute h1{}
# en xpath je vais ecrire : //h1
# avec un attribut : //tagName[@AttributeName="Value"]
# // div[@class="full-script"] ou //div[@id="viny"]
# on l'utilisera avec selenium : driver.find_elements_by_xpath()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Recaptcha bloque le code, google reconnait selenium comme un robot

# On crée un simulateur de navigateur web, ici Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# On connecte le simulateur à Google
driver.get("https://www.google.com/")

# On détecte le bouton "Accepter les cookies"
cookiebutton = driver.find_element(by=By.ID, value="L2AGLb")

# On clique sur ce bouton
cookiebutton.click()

# On patiente quelques secondes que la page se charge entièrement
sleep(3)

# On détecte la barre de recherche de Google
search = driver.find_element(by=By.NAME, value="q")

# On y entre le texte Selenium, puis on appuie sur Entrée
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)
sleep(3)

# On scrolle tout en bas de la page pour charger la deuxième page de résultats
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)

# On détecte tous les éléments HTML de balise h3 (qui contiennent les titres des résultats de recherche Google)
links2 = driver.find_elements(by=By.TAG_NAME, value="h3")

# On affiche les textes de ces résultats
for x in links2:
    print(x.text)




## problème car le code ne finit pas son execution a cause de je ne suis pas un robot : 
# reCAPTCHA de google