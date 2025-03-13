# cas pour une course
# construction d'un code scraping pour recuperer les données (info) sur une course

from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

# creation du df de stockage

columns = ["Rank", "Previous Rank", "Diff", "Rider", "Rider link","Team", "Points"]
df_riders = pd.DataFrame(columns=columns)

# url de base pour recuperer la liste des joueurs
# comme on veut les 500 premiers, il y a un filtre sur la page
# on va juste faire une liste de url et faire une boucle de tout le code de quand on a unr url

urls = [
    "https://www.procyclingstats.com/rankings.php", 
    "https://www.procyclingstats.com/rankings.php?nation=&age=&zage=&page=smallerorequal&team=&offset=100&teamlevel=&filter=Filter",
    "https://www.procyclingstats.com/rankings.php?nation=&age=&zage=&page=smallerorequal&team=&offset=100&teamlevel=&filter=Filter",
    "https://www.procyclingstats.com/rankings.php?nation=&age=&zage=&page=smallerorequal&team=&offset=100&teamlevel=&filter=Filter",
    "https://www.procyclingstats.com/rankings.php?nation=&age=&zage=&page=smallerorequal&team=&offset=100&teamlevel=&filter=Filter"
    ]

for url in urls:
    req = requests.get(url)

    ## formatage avec beautifulsoup on utilise le parser(formateur) : html

    page = BeautifulSoup(req.text, "html.parser") 

    ## scraping 500 premiers riders
    tab = page.find("table")
    tab_body = tab.find("tbody")
    lines = tab_body.find_all("tr")
    for line in lines:
        data = line.find_all("td")
        resdata = []
        for datum in data:
            a_tag = datum.find("a")
            if a_tag and "href" in a_tag.attrs:
                link = a_tag["href"]
                text = a_tag.text.strip() # recupere le nom
                # pour ne recuperer que le lien du rider on va utiliser startswith
                if link.startswith("rider/"):
                    full_link = f"https://www.procyclingstats.com/{link}"
                    resdata.append(text)
                    resdata.append(full_link)
                else:
                    # dans le cas où c'est pas le href d'un rider, on ajoute juste le texte du lien
                    resdata.append(text)
            else:
                resdata.append(datum.text.strip())


        # enlever la donnée H2Hgoto, c'est juste un lien, pas une donnée utile
        resdata.pop(3)
        # ajout des données dans df

        df_riders.loc[len(df_riders)] = resdata

        # on reinitialise resdata, pour gagner en mémoire

        resdata = []
print(df_riders.head())
print(df_riders.shape)
path_data = r"C:\Users\nakav\OneDrive - Université Clermont Auvergne\2A\collecte_auto_donnees\S4\projet\data"
df_riders.to_excel(f"{path_data}/top_500_riders.xlsx")
