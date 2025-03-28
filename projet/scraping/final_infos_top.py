import pandas as pd
# ici on va faire filtrer les 500 du top pour ne recueprer que ceux faisant 
# partie des top 10 de chaque course
path_data = r"C:\Users\nakav\OneDrive - Université Clermont Auvergne\2A\collecte_auto_donnees\S4\projet\data"

# Charger les deux fichiers dans des DataFrames
df1 = pd.read_csv(f"{path_data}/infos_riders.csv", sep=';')  # Charger le fichier CSV avec ';' comme séparateur
df2 = pd.read_excel(f"{path_data}/top_10_concatene.xlsx")   # Charger le deuxième fichier CSV avec ';'


print("Colonnes du premier fichier (csv) :", df1.columns)

print()

print("Colonnes du deuxième fichier (excel) :", df2.columns)



