import pandas as pd
import os

# Dossier contenant les fichiers Excel
path_data = "C:/Users/nakav/OneDrive - Université Clermont Auvergne/2A/collecte_auto_donnees/S4/projet/data/top_10"  # Remplacez par votre chemin

# Liste de tous les fichiers Excel dans le dossier
files = [f for f in os.listdir(path_data) if f.endswith('.xlsx')]

# Liste pour stocker les DataFrames
dfs = []


# Dictionnaire associant les noms abrégés aux vrais noms de course
race_name_mapping = {
    "top_10_riders_tour-de-france_2024_gc": "Tour de France",
    "top_10_riders_giro-d-italia_2024_gc": "Giro d'Italia",
    "top_10_riders_vuelta-a-espana_2024_gc": "La Vuelta ciclista a España",
    "top_10_riders_world-championship_2024_result": "World Championships",
    "top_10_riders_amstel-gold-race_2024_result": "Amstel Gold Race",
    "top_10_riders_milano-sanremo_2024_result": "Milano-Sanremo",
    "top_10_riders_tirreno-adriatico_2024_gc": "Tirreno-Adriatico",
    "top_10_riders_liege-bastogne-liege_2024_result": "Liege-Bastogne-Liege",
    "top_10_riders_il-lombardia_2024_result": "Il Lombardia",
    "top_10_riders_la-fleche-wallone_2024_result": "La Flèche Wallonne",
    "top_10_riders_paris-nice_2024_gc": "Paris - Nice",
    "top_10_riders_paris-roubaix_2024_result": "Paris-Roubaix",
    "top_10_riders_volta-a-catalunya_2024_gc": "Volta Ciclista a Catalunya",
    "top_10_riders_dauphine_2024_gc": "Criterium du Dauphine",
    "top_10_riders_ronde-van-vlaanderen_2024_result": "Tour des Flandres",
    "top_10_riders_Gent-Wevelgem_2024_result": "Gent-Wevelgem in Flanders Fields",
    "top_10_riders_San-Sebastián_2024_result": "Clásica Ciclista San Sebastián"
}


# Importer chaque fichier et ajouter une colonne "Course"
for file in files:
    # Lire le fichier Excel
    file_path = os.path.join(path_data, file)
    df = pd.read_excel(file_path)
    
    # Extraire le nom de la course à partir du nom du fichier (sans extension)
    course_name = os.path.splitext(file)[0]
    
    # Ajouter une colonne "Course"
    df['Course'] = race_name_mapping[course_name]
    
    # Ajouter le DataFrame à la liste
    dfs.append(df)

# Concatenation de tous les DataFrames
df_final = pd.concat(dfs, ignore_index=True)


# on constate que dans Rider on a le nom du coureur et de son equipe on va juste garder le nom du rider
df_final['Rider'] = df_final.apply(lambda row: row['Rider'].replace(row['Team'], '').strip(), axis=1)



# Sauvegarder le DataFrame final en un fichier Excel
output_path = "C:/Users/nakav/OneDrive - Université Clermont Auvergne/2A/collecte_auto_donnees/S4/projet/data/top_10_concatene.xlsx"
df_final.to_excel(output_path, index=False)

print(f"Fichier concaténé enregistré sous : {output_path}")
