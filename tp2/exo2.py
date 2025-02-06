import requests    # pour la requette http get pour recuper le code brute html de la page
from bs4 import BeautifulSoup     # pour transformer le code brute afin de recuperer, modifier du contenu
import pandas as pd

url_api ="https://fr.wikipedia.org/wiki/Liste_des_monarques_de_France"

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
colum = ["Vue d'artiste", "Nom", "Début du règne", "Fin du règne", "Notes"]
df.columns = colum
df = df.iloc[1:]
print(df.head())



