# scraping des données des riders

from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl


# liste des races
races_original_name = [
    "Tour de France",
    "Giro d'Italia",
    "La Vuelta ciclista a España",
    "World Championships",
    "Amstel Gold Race",
    "Milano-Sanremo",
    "Tirreno-Adriatico",
    "Liege-Bastogne-Liege",
    "Il Lombardia",
    "La Flèche Wallonne",
    "Paris - Nice",
    "Paris-Roubaix",
    "Volta Ciclista a Catalunya",
    "Criterium du Dauphine",
    "Tour des Flandres",
    "Gent-Wevelgem in Flanders Fields",
    "Clásica Ciclista San Sebastián"
]


races = [
    "tour-de-france/2024/gc",
    "giro-d-italia/2024/gc",
    "vuelta-a-espana/2024/gc",
    "world-championship/2024/result",
    "amstel-gold-race/2024/result",
    "milano-sanremo/2024/result",
    "tirreno-adriatico/2024/gc",
    "liege-bastogne-liege/2024/result",
    "il-lombardia/2024/result",
    "la-fleche-wallone/2024/result",
    "paris-nice/2024/gc",
    "paris-roubaix/2024/result",
    "volta-a-catalunya/2024/gc",
    "dauphine/2024/gc",
    "ronde-van-vlaanderen/2024/result",
    "Gent-Wevelgem/2024/result",
    "San-Sebastián/2024/result"
]



# url de base

url = "https://www.procyclingstats.com/"

# collecte de données des courses

## pour passer aux infos de la course pour l'année 2024 on ajoute race/nom/race/2024/gc

url_race = url+f"race/{races[0]}"
print(url_race)
req = requests.get(url_race)

## formatage avec beautifulsoup on utilise le parser(formateur) : html

page = BeautifulSoup(req.text, "html.parser") 


## extraire les infos
info_race_ul = page.find(class_="infolist")
info_race_il = info_race_ul.find_all("li")

## scaping code auto

info_race = []
info_race.append(f"Nom:{races_original_name[0]}")
for i in range(len(info_race_il)):
    info_race.append(info_race_il[i].text.strip())


## scraping top 10 riders
## class table : results basic moblist11
# Récupérer toutes les tables ayant 'results basic' dans la classe
"""tab = page.find("table")
tab_body = tab.find("tbody")
lines = tab_body.find("tr")
data = lines.find_all("td")
resdata = []
for datum in data:
    resdata.append(datum.text.strip())
print(resdata)"""


tab = page.find("table")  # Trouver la table
tab_body = tab.find("tbody")  # Trouver le corps du tableau
lines = tab_body.find_all("tr")  # Récupérer toutes les lignes

resdata = []
for line in lines:
    data = line.find_all("td")  # Récupérer toutes les colonnes
    row_data = [td.get_text(strip=True) for td in data]  # Extraire le texte proprement
    if row_data:  # Ignorer les lignes vides
        resdata.append(row_data)

print(resdata[0])


"""for line in lines[:10]:
    data = line.find_all("td")
    rider_name = data[1].text.strip()
    resline.append(rider_name)"""


"""print(resline)
"""

values = [
    ":".join(item.split(":")[1:]).strip() if ":" in item and ":".join(item.split(":")[1:]).strip() else None
    for item in info_race
]





