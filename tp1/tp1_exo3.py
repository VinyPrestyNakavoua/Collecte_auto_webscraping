import requests
import pandas as pd


url_api1 ="https://collectionapi.metmuseum.org/public/collection/v1/objects"

req = requests.get(url_api1)

wb = req.json()
df_id = pd.json_normalize(wb)
df_id = df_id["objectIDs"]
df_id = df_id[0]   # ceci permet d'avoir la liste exhaustive des collections

# avec le code ci-dessus, on recupère simplement le nombre total des collections du musée et 
# l'id de chaque objet, mais pour avoir les infos sur une ressourche, il faut faire ceci:

# exemple : pour l'objet id = 2
# maintenant on va se servir du code ci-dessus pour avoir la liste des id objets qu'on va faire passer
# dans l'url ci-dessous à l'aide d'une boucle
data = []

# en vrai ce qu'on souhaiterait c'est faire tourner 3 vm pour gagner du temps
# on va exécuter ce code dans ces 3 vm pour recuperer des données et en faisons juste varier l'indice
# mais bon on va alors faire aevec une seule machine et faire varier l'indice df_id[] 3 fois
for id in df_id[300:1000]:
    url_api2 ="https://collectionapi.metmuseum.org/public/collection/v1/objects/{}".format(id)

    req = requests.get(url_api2)

    # si la requete est valide, on fait ce qui suit : repere les infos en json puis on les stocke dans data
    if req.status_code == 200:
        wb = req.json()
        df = wb  # on va juste ajouter des json dans la liste comme ça, je vais faire un pdf normalize a la fin

        # le resultat est un json dans quoi je vais le stocker, pour facilement faire des analyses
        # essayons dans un json
        data.append(df)


df = pd.json_normalize(data)


# exportation de df
df.to_csv("objects_info_300-1000.csv", index=False, encoding="utf-8")




