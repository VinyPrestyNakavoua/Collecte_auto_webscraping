import pandas as pd
from bs4 import BeautifulSoup
import requests

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

#races = ["tour-de-france/2024/gc"]
path_data = r"C:\Users\nakav\OneDrive - Université Clermont Auvergne\2A\collecte_auto_donnees\S4\projet\data"


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
url = "https://www.procyclingstats.com/"

# Définition des colonnes
columns = [
    "Classement", "Dossard", "Écart", "Points UCI", "Bonus", "Type coureur", "Nom", "Âge",
    "Équipe", "Points PCS", "Points UCI Total", "Autre", "Temps total", "Vitesse Moyenne"
]

time_ar = [
    "83:38:56",
    "79:14:03",
    "81:49:18",
    "6:27:30",
    "5:58:17",
    "6:14:44",
    "26:22:23",
    "6:13:48",
    "6:04:58",
    "4:40:24",
    "27:50:23",
    "5:25:58",
    "28:21:29",
    "25:35:40",
    "6:05:17",
    "5:36:00",
    "5:46:12"
]

# Création du DataFrame
df = pd.DataFrame(columns=columns)

# Collecte des données
for i in range(len(races)):
    url_race = url + f"race/{races[i]}"
    print(f"Scraping : {url_race}")

    req = requests.get(url_race)
    page = BeautifulSoup(req.text, "html.parser")

    # Sélection du tableau
    tab = page.find("table", class_=["results basic moblist10", "results basic moblist11"])
    if tab:

        # creation du dataframe pour chaque course
        # Extraire les noms des colonnes depuis <thead>
        thead = tab.find("thead")
        if thead:
            columns = [th.text.strip() for th in thead.find_all("th")]
        else:
            columns = []  # Si pas de thead, éviter l'erreur

        # Créer le DataFrame avec ces colonnes
        df = pd.DataFrame(columns=columns)

        # extraire les infos dans le tbody

        tbody = tab.find("tbody")
        if tbody:
            resline = []
            
            # Récupérer les 10 premières lignes
            lines = tbody.find_all("tr")[:10]
            for line in lines:
                data = line.find_all("td")
                resdata = [datum.text.strip() for datum in data]
                #resdata.append(races_original_name[i])
                resline.append(resdata)

            # Ajouter au DataFrame
            df.loc[len(df)] = resline
            df.to_excel(f"{path_data}/top_10_riders{races[i]}.xlsx")



    else:
        print("Tableau non trouvé !")


# Sauvegarde en Excel

print("Scraping terminé. Données enregistrées.")



