# cas pour une course
# construction d'un code scraping pour recuperer les données (info) sur une course

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
    "tour-de-france",
    "giro-d-italia",
    "vuelta-a-espana",
    "world-championship",
    "amstel-gold-race",
    "milano-sanremo",
    "tirreno-adriatico",
    "liege-bastogne-liege",
    "il-lombardia",
    "la-fleche-wallone",
    "paris-nice",
    "paris-roubaix",
    "volta-a-catalunya",
    "dauphine",
    "ronde-van-vlaanderen",
    "Gent-Wevelgem",
    "San Sebastián"
]


# url de base

url = "https://www.procyclingstats.com/"

# collecte de données des courses

## pour passer aux infos de la course pour l'année 2024 on ajoute race/nom/race/2024/gc

url_race = url+f"race/{races[3]}/2024/result"
print(url_race)
req = requests.get(url_race)

## formatage avec beautifulsoup on utilise le parser(formateur) : html

page = BeautifulSoup(req.text, "html.parser") 


## extraire les infos
info_race_ul = page.find(class_="infolist")
info_race_il = info_race_ul.find_all("li")

# urls for scraping
info_race = []
info_race.append(f"Nom:{races_original_name[0]}")
for i in range(len(info_race_il)):
    info_race.append(info_race_il[i].text.strip())


# scaping code auto


values = [
    ":".join(item.split(":")[1:]).strip() if ":" in item and ":".join(item.split(":")[1:]).strip() else None
    for item in info_race
]

print(values)
"""
# Liste des colonnes
columns = [
    "Nom",
    "Date",
    "Start time",
    "Avg. speed winner",
    "Classification",
    "Race category",
    "Distance",
    "Points scale",
    "UCI scale",
    "Parcours type",
    "ProfileScore",
    "Vertical meters",
    "Departure",
    "Arrival",
    "Race ranking",
    "Startlist quality score",
    "Won how",
    "Avg. temperature"
]

# Création du DataFrame vide
df = pd.DataFrame(columns=columns)

df.loc[len(df)] = values

df.to_excel("race.xlsx")
"""