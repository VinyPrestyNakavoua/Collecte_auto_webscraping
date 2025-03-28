import pandas as pd

path_data = r"C:\Users\nakav\OneDrive - Université Clermont Auvergne\2A\collecte_auto_donnees\S4\projet\data"

# Charger les deux fichiers dans des DataFrames
df1 = pd.read_csv(f"{path_data}/top_500_riders.csv", sep=';')  # Charger le fichier CSV avec ';' comme séparateur
df2 = pd.read_csv(f"{path_data}/cyclists_2024.csv", sep=';')   # Charger le deuxième fichier CSV avec ';'

# Vérification des colonnes et types des données
print("Colonnes du premier fichier (csv) :", df1.columns)
print("Colonnes du deuxième fichier (CSV) :", df2.columns)

df1.drop(columns=['Previous Rank', 'Diff', 'Rider link', 'Team'], inplace=True)

print()
print()

print("Colonnes du premier fichier (csv) :", df1.columns)
print("Colonnes du deuxième fichier (CSV) :", df2.columns)

# Effectuer la jointure (cbind) en utilisant la colonne clé 'Rank'
df_merged = pd.merge(df1, df2, on='Rank', how='inner')  # 'Rank' est la colonne clé pour la jointure

# Sauvegarder le DataFrame combiné dans un nouveau fichier CSV
df_merged.to_csv(f"{path_data}/infos_riders.csv", index=False)

# Afficher le résultat (les premières lignes pour vérification)
print(df_merged.head())


