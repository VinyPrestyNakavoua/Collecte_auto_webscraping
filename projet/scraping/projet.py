# https://www.procyclingstats.com/
# c'est un site qui presente les stats sur le cyclisme
# Les données qu'on doit récupérer : les top 10 de chaque course, 
# les infos des courses (distance, vitesse moyenne, dénivelé), 
# et les infos des coureurs (pays, taille poids, age, equipe, notes, 
# classements mondiaux)
# note : pas d'utilisation d'api, juste scraper

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


# Creation du df qui contiendra les données
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


# collecte de données des courses

## pour passer aux infos de la course pour l'année 2024 on ajoute race/nom/race/2024/gc
for i in range(len(races)):
    url_race = url+f"race/{races[i]}"
    print(url_race)
    req = requests.get(url_race)

    ## formatage avec beautifulsoup on utilise le parser(formateur) : html

    page = BeautifulSoup(req.text, "html.parser") 


    ## extraire les infos
    info_race_ul = page.find(class_="infolist")
    info_race_il = info_race_ul.find_all("li")

    # urls for scraping
    info_race = []
    info_race.append(f"Nom:{races_original_name[i]}")
    for j in range(len(info_race_il)):
        info_race.append(info_race_il[j].text.strip())


    # scaping code auto


    values = [
        ":".join(item.split(":")[1:]).strip() if ":" in item and ":".join(item.split(":")[1:]).strip() else None
        for item in info_race
    ]


    df.loc[len(df)] = values
    # remettre values à zero
    values = []
    info_race = []


df.to_excel("race.xlsx")
