# scraper les données sur les 10 riders le top 10 de chaque course

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

# il y a des courses qui ont gc (classification generale) car elles se font sur plusieurs jours (stage)
# les courses ayant result sont celles qui se font en un seul jour c'est pourquoi il y a result (no stage)


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
# Définition des colonnes
columns = [
    "Classement", "Dossard", "Écart", "Points UCI", "Bonus", "Type coureur", "Nom", "Âge", 
    "Équipe", "Points PCS", "Points UCI Total", "Autre", "Temps total", "Vitesse Moyenne"
]

# Création du DataFrame
df = pd.DataFrame(columns=columns)
# collecte de données des courses

## pour passer aux infos de la course pour l'année 2024 on ajoute race/nom/race/2024/gc
#for i in range(len(races)):
i=3
url_race = url+f"race/{races[i]}"
print(url_race)
req = requests.get(url_race)

## formatage avec beautifulsoup on utilise le parser(formateur) : html

page = BeautifulSoup(req.text, "html.parser") 

print(req)

tab = page.find("table", class_=["results basic moblist10", "results basic moblist11"])
tbody = tab.find("tbody")
resline = []
lines = tbody.find_all("tr")[:10]
for line in lines:
    data = line.find_all("td")
    resdata = []
    for datum in data:
        resdata.append(datum.text.strip())
    print(resdata)
    resline.append(resdata)
    #df.loc[len(df)] = resline


#print(resline)
for i in range(len(resline)):
    print(len(resline[i]))

#ath_data = r"C:\Users\nakav\OneDrive - Université Clermont Auvergne\2A\collecte_auto_donnees\S4\projet\data"
#df.to_excel(f"{path_data}/top_10_riders.xlsx")




