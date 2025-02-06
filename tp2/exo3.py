from bs4 import BeautifulSoup
import pandas as pd
import requests

# chatgpt me propose d'utilise l'api de ibdm : insdustrie du cinema qui a une api
# mais je vais juste le faire avec wikipedia
# je vais me servir de mon code dictionnaire de l'exo5 et le modifier un peu pour renvoyer la liste
# des films

def actor(acteur):
    url = f"https://fr.wikipedia.org/wiki/{acteur}"
    req = requests.get(url)
    page = BeautifulSoup(req.text, "html.parser")

    # les films sont listés avec la balise ul, li, i

    ul = page.find_all("ul")  # liste des ul
    res = []
    for i in range(len(ul)):
        li = ul[i].find_all("li")  # pour chaque ul, liste des li
        for j in range(len(li)):    
            tag_a = li[j].find_all("a")
            # pour chaque li, liste des a
            res_temp = []
            for k in range (len(tag_a)):
                titre = tag_a[k].text
                res_temp.append(titre)
            res.append(res_temp)
    
    res_f = []
    for i in range(len(res)):
        f = ""
        for j in range(len(res[i])):
            f = f + res[i][j] + " "
            res_f.append(f)
    return res_f



def verify_actor(actor1, actor2):
    film1= actor(actor1)
    film2 = actor(actor2)

    # verifier s'ils ont un film en commun



    












