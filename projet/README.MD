# Collecte de données cyclistes à partir de ProCyclingStats pour Power BI
## Description du projet
Ce projet a pour objectif de collecter des données cyclistes depuis le site web ProCyclingStats pour l'année 2024, notamment :

1. Les Top 10 des résultats de chaque course.
2. Les détails de chaque course (date, heure de départ, vitesse moyenne, distance, classement, catégorie de course, etc.).
3. Les informations des coureurs (date de naissance, nationalité, poids, taille, équipe, classement mondial UCI, etc.).
4. Ces données seront ensuite stockées dans une base de données PostgreSQL, puis utilisées dans Power BI pour effectuer des analyses et créer des visualisations.

## Structure du projet
1. Scraper les données à partir de ProCyclingStats en utilisant BeautifulSoup et requests.
2. Insérer les données collectées dans une base de données PostgreSQL.
3. Analyser les données dans Power BI.