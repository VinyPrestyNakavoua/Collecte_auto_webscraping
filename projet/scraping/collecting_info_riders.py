
import requests
import pandas as pd
import bs4
import time
import random

path_data = r"C:\Users\nakav\OneDrive - Université Clermont Auvergne\2A\collecte_auto_donnees\S4\projet\data"


def get_pcs_points(html):
    """Récupère les points PCS pour 2024."""
    try:
        h3 = html.find_all("h3")
        ranking = None
        for title in h3:
            if title.string == "PCS Ranking position per season":
                ranking = title.parent.find("table")
                break
        table = ranking.find("tbody")
        for row in table.find_all("tr"):
            if row.find("td").string == "2024":
                return int(row.find("div", class_="vTitle").string)
    except:
        return None

def get_speciality_points(html):
    """Récupère les points PCS par spécialité."""
    rankings = []
    try:
        h4 = html.find_all("h4")
        for title in h4:
            if title.string == "Points per specialty":
                for li in title.parent.find_all("li"):
                    rankings.append(int(li.find("div", class_="pnt").string))
                break
    except:
        return [None] * 5  # Retourne une liste de None si erreur
    return rankings

def get_2024_team(html):
    """Récupère l'équipe 2024 du coureur."""
    try:
        h3 = html.find_all("h3")
        for title in h3:
            if title.string == "Teams":
                teams = title.parent.parent.find_all("div")[1]
                break
        for li in teams.find_all("li"):
            if li.find("div", class_="season").string == "2024":
                return li.find("a").string
    except:
        return None

def scrape_cyclists_2024(max_cyclists=500):
    """Scrape les données des 500 meilleurs coureurs 2024."""
    base_url = "https://www.procyclingstats.com/"
    cyclist_links = []
    
    # Récupération de la liste des coureurs
    for offset in range(0, max_cyclists, 100):
        url = f"https://www.procyclingstats.com/rankings.php?offset={offset}"
        req = requests.get(url)
        page = bs4.BeautifulSoup(req.text, "html.parser")
        
        for link in page.find_all("a", href=True):
            if link["href"].startswith("rider/"):
                cyclist_links.append(base_url + link["href"])
    
    # Récupération des données détaillées
    data = []
    for idx, url in enumerate(cyclist_links[:max_cyclists]):
        print(f"Scraping {idx+1}/{max_cyclists}: {url}")
        req = requests.get(url)
        page = bs4.BeautifulSoup(req.text, "html.parser")
        time.sleep(random.uniform(1, 3))  # Pause aléatoire
        
        try:
            div = page.find("div", class_="rdr-info-cont")
            infos = div.get_text() if div else ""
            
            dob = infos.split("birth: ")[1].split("(")[0] if "birth:" in infos else None
            nationality = infos.split("Nationality: ")[1].split("Weight")[0].strip() if "Nationality:" in infos else None
            weight = infos.split("kg")[0][-2:].strip() if "kg" in infos else None
            height = infos.split("Height: ")[1].split("m")[0].strip() if "Height:" in infos else None
            
            pcs_points = get_pcs_points(page)
            specialty_points = get_speciality_points(page)
            team_2024 = get_2024_team(page)
            
            data.append([
                idx + 1, dob, nationality, weight, height, pcs_points, *specialty_points
            ])
        except Exception as e:
            print(f"Erreur sur {url}: {e}")
            continue
    
    # Création du DataFrame
    df = pd.DataFrame(data, columns=[
        "Rank", "Date_of_birth", "Nationality", "Weight", "Height", "PCS_points",
        "One_day_races", "GC", "Time_trial", "Sprint", "Climber", "Hills"
    ])
    
    df.to_csv(f"{path_data}/cyclists_2024.csv", index=False, sep=";")
    print("Scraping terminé. Données enregistrées dans cyclists_2024.csv")

# Lancer le scraping
scrape_cyclists_2024()
