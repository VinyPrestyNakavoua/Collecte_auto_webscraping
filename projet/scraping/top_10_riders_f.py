import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

# Liste des courses
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

# Nom original des courses
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

# URL de base
url_base = "https://www.procyclingstats.com/race/"

# Dossier de sauvegarde
path_data = r"C:\Users\nakav\OneDrive - Université Clermont Auvergne\2A\collecte_auto_donnees\S4\projet\data"
os.makedirs(path_data, exist_ok=True)  

# Collecte des données
for i in range(len(races)):
    race_url = url_base + races[i]
    print(f"Scraping : {race_url}")

    
    # on se propose ces controles http pour mieux suivre l'exécution du code
    try:
        req = requests.get(race_url, timeout=10)  
        req.raise_for_status()  
    except requests.RequestException as e:
        print(f"Erreur de requête pour {race_url} : {e}")
        continue 

    
    # entrer de beautifulsoup
    page = BeautifulSoup(req.text, "html.parser")

    # Sélection du tableau (avec plusieurs classes possibles)
    # parce que le tableau des courses ne portent pas le meme nom de classe
    tab = page.find("table", class_=["results basic moblist10", "results basic moblist11"])
    
    if not tab:
        print(f"Tableau non trouvé pour {races_original_name[i]}")
        continue

    # Extraire les noms des colonnes depuis <thead>
    # comme les courses n'ont pas les memes filtres, pas les memes colonnes 
    # on va juste creer un df pour chaque course dont les colonnes seront les entetes des tableaux
    thead = tab.find("thead")
    if thead:
        columns = [th.text.strip() for th in thead.find_all("th")]
    else:
        print(f"Pas de thead trouvé pour {races_original_name[i]}")
        continue

    # Créer un DataFrame pour cette course
    df = pd.DataFrame(columns=columns)

    # Extraire les données de <tbody>
    tbody = tab.find("tbody")
    if tbody:
        rows = tbody.find_all("tr")[:10]  # Top 10 riders
        for row in rows:
            data = [td.text.strip() for td in row.find_all("td")]
            try:
                df.loc[len(df)] = data 
            except Exception as e:
                print(f"erreur avec l'url :  {race_url} -> {e}" )

    # Nettoyage du nom du fichier pour éviter les caractères interdits
    filename = races[i].replace("/", "_")
    file_path = os.path.join(path_data, f"top_10_riders_{filename}.csv")

    # Sauvegarde en CSV
    # le nombre de colonnes varie selon les courses du coup en cas d'erreur
    # on va continuer  à scraper les données des autres courses
    df.to_csv(file_path, index=False, encoding="utf-8")
    print(f"Données enregistrées : {file_path}")

print("✅ Scraping terminé !")
