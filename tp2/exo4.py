# on a proposer une fonction qui va générer un fichier csv
# proposant affichant les titres et les liens vers les infos du jour de trois sites

import requests   
from bs4 import BeautifulSoup 
import pandas as pd

# pour recuperer le lien : a["href"], le titre : a["title"]
# comment peut-on faire en sorte de ne recuperer que les trois premieres infos


def bfm():
    # cette fonction est juste pour bfm car les autres sites d'infos n'ont probablement pas les memes
    # noms de classes, et encore la meme structure de code ou simplement le meme DOM
    url_api = "https://www.bfmtv.com/"
    url_api_to_link = "https://www.bfmtv.com"
    req = requests.get(url_api)

    page = BeautifulSoup(req.text, "html.parser")  

    res = []

    # pour recuperer le lien : a["href"], le titre : a["title"]
    article = page.find("article", class_="une_item icon_big content_item")
    tag_a = article.find("a")
    lien = tag_a["href"]
    titre = tag_a["title"]
    res.append([titre, url_api_to_link+lien])


    div_principal = page.find(class_="block_fleuve icon_middle")
    article = div_principal.find_all("article", limit=2)
    for i in range(2):
        tag_a = article[i].find("a")
        lien = tag_a["href"]
        titre = tag_a["title"]
        res.append([titre, url_api_to_link+lien])

    # creation de la dataframebfm
    df = pd.DataFrame(res)
    columns = ["Titre", "lien"]
    df.columns = columns
    df.to_csv("3_last_news_of_bfm.csv")
    return df



# pour cnews, c'est encore plus simple
# on a dans div wrapper-content : 3 infos presentees
# pour le lien on ira dans la div : class="dm-news-item-3  associated-video"
# et on va recuperer tous les liens 
# titre est dans une balise h2 de class="dm-tag-title"

def cnews():
    url_api = "https://www.cnews.fr/"
    url_api_to_link = "https://www.cnews.fr"
    req = requests.get(url_api)
    page = BeautifulSoup(req.text, "html.parser")
    div_principale = page.find(class_="wrapper-content")
    tag_div = div_principale.find_all("div", limit=3)
    res = []
    for i in range(3):
        tag_a = tag_div[i].find("a")
        lien = tag_a["href"]
        titre = tag_div[i].find("h2", class_="dm-tag-title").text
        res.append([titre, url_api_to_link+lien])
    
    return res



def lemonde():
    url_api = "https://www.lemonde.fr/actualite-en-continu/"
    url_api_to_link = "https://www.lemonde.fr/actualite-en-continu"
    req = requests.get(url_api)
    page = BeautifulSoup(req.text, "html.parser")
    section_principal = page.find(class_="river river--en-continu river--short old__river")
    subsections = section_principal.find_all("section", limit=3)
    res = []
    for i in range(3):
        seci = subsections[i]
        tag_a = seci.find("a")
        lien = tag_a["href"]
        tag_h3 = seci.find("h3", class_="teaser__title")
        titre = tag_h3.text
        res.append([titre, url_api_to_link+lien])

    # creation de la dataframe
    df = pd.DataFrame(res)
    columns = ["Titre", "lien"]
    df.columns = columns
    df.to_csv("3_last_news_of_lemonde.csv")
    return df





res = lemonde()
print(res)

