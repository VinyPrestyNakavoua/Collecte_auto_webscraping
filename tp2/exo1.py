# on peut vouloir recuperer des donnees sur une page web sans avoir necessairement besoin d'une api
# en plus très souvent on va utiliser les api quand on va recuperer les donnees sur un serveur
# et du coup pour les donnees presentes sur une page web, on va faire du web scrapping

import requests    # pour la requette http get pour recuper le code brute html de la page
from bs4 import BeautifulSoup     # pour transformer le code brute afin de recuperer, modifier du contenu
import pandas as pd

url_api ="https://fr.wikipedia.org/wiki/Liste_des_pays_par_population"

# requete get
req = requests.get(url_api)

# On utilise beautifulsoup pour formater le code source
page = BeautifulSoup(req.text, "html.parser")  # on utilise le parser(formateur) : html

# il  y a HTML, XML ou JSON parsers, on prefere html c'est plus simple pour python


# exemple : recuperons la table presente sur cette page
tab = page.find("table")

resline = []
for line in tab.find_all("tr"):
    data = line.find_all("td")
    resdata = []
    for datum in data:
        resdata.append(datum.text.strip())

    resline.append(resdata)

# les etapes en dessous sont necessaires pour avoir un bon format : dataframe
df = pd.DataFrame(resline)
colum = ["Rang(2021)", "Pays ou territoire", "Population au juillet 2021", "Population projetée au 1er janvier 2025"]
df.columns = colum
df.index = df["Rang(2021)"] 
df = df.drop("Rang(2021)", axis=1)
df = df.iloc[1:]
print(df.head())


print()
print()

# exo1 : 
# Afficher la liste des liens présents dans la page wikipedia proposée dans l’exemple.
# page a deja ete formate avec beautifulsoup du coup on peut acceder aux elements html
# a['href'] : recupere le lien
links = [a['href'] for a in page.find_all("a", href=True)]
for link in links[:10]:
    print(link)



