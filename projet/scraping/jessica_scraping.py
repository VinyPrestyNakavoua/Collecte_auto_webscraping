from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.carburants.org/prix-carburants/cantal.15/aurillac.zzaaw/carrefour_aureldis-carrefour.ExEjDj"


req = requests.get(url)

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

print(resline)




