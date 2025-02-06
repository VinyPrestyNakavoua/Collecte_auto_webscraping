import requests
import pandas as pd


url_api1 ="https://collectionapi.metmuseum.org/public/collection/v1/objects"

req = requests.get(url_api1)

wb = req.json()
df = pd.json_normalize(wb)
df = df["objectIDs"]
objet = df[0]   # ceci permet d'avoir la liste exhaustive des collections

# avec le code ci-dessus, on recupère simplement le nombre total des collections du musée et 
# l'id de chaque objet, mais pour avoir les infos sur une ressourche, il faut faire ceci:

# exemple : pour l'objet id = 2
# maintenant on va se servir du code ci-dessus pour avoir la liste des id objets qu'on va faire passer
# dans l'url ci-dessous à l'aide d'une boucle
data = {}

for id in objet[:10]:
    url_api2 ="https://collectionapi.metmuseum.org/public/collection/v1/objects/{}".format(id)

    req = requests.get(url_api2)

    wb = req.json()
    df = pd.json_normalize(wb)

    # le resultat est un json dans quoi je vais le stocker, pour facilement faire des analyses
    # essayons dans un json
    data[id] = df


print(data)



