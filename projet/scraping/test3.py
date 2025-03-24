from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL de base
url_base = "https://www.procyclingstats.com/"

# Liste des courses à scraper
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
    "gent-wevelgem/2024/result",
    "san-sebastian/2024/result"
]

# Colonnes du DataFrame
columns = ["Classement", "Nom", "Équipe", "Temps", "Écart", "Course"]

# Création du DataFrame vide
df = pd.DataFrame(columns=columns)

# Scraper chaque course
for race in races:
    url_race = url_base + f"race/{race}"
    print(f"Scraping: {url_race}")

    # Requête HTTP
    req = requests.get(url_race)

    # Vérification du statut de la requête
    if req.status_code != 200:
        print(f"❌ Erreur {req.status_code} pour {race}")
        continue

    # Parsing de la page
    page = BeautifulSoup(req.text, "html.parser")

    # Sélection de la classe de tableau appropriée
    table_class = "results basic moblist11" if "paris-roubaix" in race or "ronde-van-vlaanderen" in race else "results basic moblist10"

    # Recherche du tableau des résultats
    tab = page.find("table", class_=table_class)
    
    if not tab:
        print(f"❌ Tableau non trouvé pour {race}")
        continue

    tbody = tab.find("tbody")
    
    if not tbody:
        print(f"❌ Corps de tableau introuvable pour {race}")
        continue

    # Récupérer les 10 premières lignes (top 10)
    lines = tbody.find_all("tr")[:10]
    
    race_results = []
    for line in lines:
        data = line.find_all("td")
        
        if len(data) >= 5:  # Vérification du nombre de colonnes
            rank = data[0].text.strip()
            rider = data[1].text.strip()
            team = data[2].text.strip()
            time = data[3].text.strip()
            gap = data[4].text.strip()

            race_results.append([rank, rider, team, time, gap, race])

    # Ajouter les résultats au DataFrame
    df = pd.concat([df, pd.DataFrame(race_results, columns=columns)], ignore_index=True)

# Affichage des 10 premières lignes du DataFrame final
print(df.head(10))

# Export en Excel (optionnel)
df.to_excel("top10_riders.xlsx", index=False)
print("✅ Données enregistrées dans top10_riders.xlsx")
