import requests
import pandas as pd
url_api3 ="https://fr.openfoodfacts.org/api/v2/search?categories_tags=sodas"

req = requests.get(url_api3)

wb = req.json()
df = pd.json_normalize(wb["products"])
df1 = df[["product_name_fr", "nutriscore_score"]]
max_score = max(df1["nutriscore_score"] )
print(df1[df1["nutriscore_score"] == max_score])