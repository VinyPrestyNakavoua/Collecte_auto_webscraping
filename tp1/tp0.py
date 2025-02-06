import requests
import pandas as pd

url_api ="https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=biscuits&fields=generic_name&page_size=100&json=true"

# on utilise requests pour envoyer des requetes http
# vue qu'on veut juste acceder à une ressource, on utilise alors la methode get
req = requests.get(url_api)

wb = req.json()
df = pd.json_normalize(wb["products"])
print(df)

