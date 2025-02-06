import requests
import pandas as pd
import json

# Exercice 1

url_api0 ="https://fr.openfoodfacts.org/api/v0/product/7613032413491.json."

req = requests.get(url_api0)

wb = req.json()
df = pd.json_normalize(wb["product"])
print(df["product_name_fr"][0])


# Quels sont les produits correspondant aux code-barres suivant ? 5449000131805, 3155250358788, 5411188119098, 8715700407760

li_url_api = ["5449000131805", "3155250358788", "5411188119098", "8715700407760"]
li_product_name = []
for i in li_url_api:
    url_api1 = "https://fr.openfoodfacts.org/api/v0/product/{}.json".format(i)
    req = requests.get(url_api1)
    wb = req.json()
    df1 = pd.json_normalize(wb["product"])
    li_product_name.append(df1["product_name_fr"][0])
    

for i in li_product_name:
    print(i)


# 3. Combien y-a-t’il de produits de marque heudebert ? Récupérez leurs noms.
url_api2 ="https://fr.openfoodfacts.org/api/v2/search?brands_tags=heudebert"

req = requests.get(url_api2)

wb = req.json()
df = pd.json_normalize(wb["products"])
print("Row count is:", df.shape[0])
print(df["product_name_fr"])

print("question 4")
# 4. Récupérez les noms et nutriscore de tous les sodas. Quel est le produit avec le meilleur nutriscore ?
url_api3 ="https://fr.openfoodfacts.org/api/v2/search?categories_tags=sodas"

req = requests.get(url_api3)

wb = req.json()
df = pd.json_normalize(wb["products"])
print(df)
print(df[["product_name_fr", "nutriscore_score"]])




