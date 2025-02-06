# Collecte_auto_webscraping

## Webscraping : Qu’est-ce que c’est ?

Le webscraping désigne les techniques d’extraction de contenu des sites internet. C’est une pratique très utile pour toute personne souhaitant travailler sur des informations disponibles en ligne mais pas nécessairement accessibles via une API.

L’idée générale est de charger le code source d’une page web, puis d’y extraire les informations souhaitées.

### Structure d’un site web

Un site web est un ensemble de pages codées en **HTML**, un langage permettant de décrire à la fois le contenu et la structure d’une page web.

Parmi les éléments incontournables d’une page HTML, on retrouve :
- `<head>` : Contient les métadonnées et les liens vers les fichiers CSS ou JavaScript.
- `<title>` : Définit le titre de la page affiché dans l’onglet du navigateur.
- `<body>` : Contient tout le contenu visible par l’utilisateur.

Les **balises HTML** permettent de structurer le contenu. Par exemple :
- `<p>` : Définit un paragraphe.
- `<h1>`, `<h2>`, `<h3>` : Définissent les titres et sous-titres.
- `<strong>` : Met en valeur du texte en gras.
- `<em>` : Met en valeur du texte en italique.

Les balises sont généralement utilisées par paires, avec une balise ouvrante `<balise>` et une balise fermante `</balise>`.

## Webscraping en Python

De manière similaire à l’utilisation d’API, le webscraping en Python commence par une requête vers la page web cible.

La principale différence est que, plutôt que de récupérer des données pré-formatées (JSON, XML, CSV), on obtient le code brut de la page HTML, qu’il faut ensuite analyser.

Pour cela, on utilise **BeautifulSoup**, une bibliothèque qui structure les données récupérées et facilite leur extraction. D’autres outils existent, notamment **Selenium**, utile pour les pages web dynamiques.

### Installation de BeautifulSoup
```bash
pip install beautifulsoup4 requests
```

### Exemple de code
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraction des titres h1
titres = soup.find_all("h1")
for titre in titres:
    print(titre.text)
```

## Bonnes pratiques du Webscraping

Le webscraping peut causer des problèmes aux sites ciblés. Pour une approche responsable, voici quelques règles à suivre :

- **Limiter les requêtes** : Ne chargez que les pages nécessaires.
- **Insérer des pauses** : Utilisez `time.sleep()` pour éviter de surcharger les serveurs.
- **Respecter la législation** : Il est illégal de scraper des données personnelles sans consentement.
- **Respecter le fichier robots.txt** : Ce fichier (ex: `https://www.example.com/robots.txt`) précise ce qui est autorisé ou non sur un site.

## Webscraping des pages dynamiques

Les techniques précédentes fonctionnent bien pour les pages **statiques**, où les données sont directement présentes dans le code HTML.

Mais pour les pages **dynamiques**, qui utilisent JavaScript pour charger du contenu, **Selenium** est un outil plus adapté.

### Installation de Selenium
```bash
pip install selenium webdriver-manager
```

### Exemple avec Selenium
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuration du navigateur
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://example.com"
driver.get(url)

# Extraction du contenu
elements = driver.find_elements("tag name", "h1")
for element in elements:
    print(element.text)

driver.quit()
```

Selenium permet de simuler les interactions humaines avec la page : scroller, cliquer sur des boutons, remplir des formulaires, etc.

---

Avec ces outils et bonnes pratiques, vous serez en mesure de scraper efficacement des données tout en respectant les sites web ciblés.

