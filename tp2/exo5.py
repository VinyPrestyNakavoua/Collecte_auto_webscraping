# une fonction dictionnaire qui affiche la definition d'un mot
from bs4 import BeautifulSoup
import pandas as pd
import requests

def dictionnaire(mot):
    url = f"https://fr.wikipedia.org/wiki/{mot}"
    req = requests.get(url)
    page = BeautifulSoup(req.text, "html.parser")
    paragraph = page.find_all("p")
    res = []
    for i in range(len(paragraph)):
        paraprint = paragraph[i].text
        res.append(paraprint)

    for i in range(len(res)):
        print(res[i])



dictionnaire("bonjour")

