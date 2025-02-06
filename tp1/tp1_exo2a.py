
# importation des modules pour la visualisation
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# je crée une fonction qui fera le web scraping, je n'aurai qu'à changer les années
def webscraptingmeteo(start, end):
	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://archive-api.open-meteo.com/v1/archive"
	params = {
		"latitude": 44.9254,
		"longitude": 2.4398,
		"start_date": start,
		"end_date": end,
		"daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "snowfall_sum"],
		"timezone": "auto"
	}
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
	print(f"Elevation {response.Elevation()} m asl")
	print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

	# Process daily data. The order of variables needs to be the same as requested.
	daily = response.Daily()
	daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
	daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
	daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()
	daily_snowfall_sum = daily.Variables(3).ValuesAsNumpy()

	daily_data = {"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
		end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	)}

	daily_data["temperature_2m_max"] = daily_temperature_2m_max
	daily_data["temperature_2m_min"] = daily_temperature_2m_min
	daily_data["precipitation_sum"] = daily_precipitation_sum
	daily_data["snowfall_sum"] = daily_snowfall_sum

	daily_dataframe = pd.DataFrame(data = daily_data)
	return daily_dataframe

# creation des df pour les années 2023, 2013, 2003 ,1993 et 1983.
df_2023 = webscraptingmeteo("2023-01-01", "2023-12-31")
df_2013 = webscraptingmeteo("2013-01-01", "2013-12-31")
df_2003 = webscraptingmeteo("2003-01-01", "2003-12-31")
df_1993 = webscraptingmeteo("1993-01-01", "1993-12-31")
df_1983 = webscraptingmeteo("1983-01-01", "1983-12-31")


# j'ai constaté que les courbes n'etaient pas les unes sur les autres, mais plutot au
# dessus de sa plage année associée, du coup je vais ajouter un indice pour chaque dataframe
# les années ont en commun 362 jours du coup je vais creer une colonne :  0 à nrow(dataframe)

dfs = [df_2023, df_2013, df_2003, df_1993, df_1983]

for i in dfs:
	n = i.shape[0]
	i["day"] = [j for j in range(0,n)]

# concatenation des dataframes

data = pd.concat(dfs, ignore_index=True)

print(data)

# Vérifier que les colonnes 'date' sont bien au format datetime
df_2023["date"] = pd.to_datetime(df_2023["date"])
df_2013["date"] = pd.to_datetime(df_2013["date"])
df_2003["date"] = pd.to_datetime(df_2003["date"])
df_1993["date"] = pd.to_datetime(df_1993["date"])
df_1983["date"] = pd.to_datetime(df_1983["date"])

# Création du graphique
plt.figure(figsize=(12, 6))  # Taille du graphique

plt.plot(df_2023["day"], df_2023["temperature_2m_max"], label="2023", color='blue')
plt.plot(df_2013["day"], df_2013["temperature_2m_max"], label="2013", color='orange')
plt.plot(df_2003["day"], df_2003["temperature_2m_max"], label="2003", color='green')
plt.plot(df_1993["day"], df_1993["temperature_2m_max"], label="1993", color='red')
plt.plot(df_1983["day"], df_1983["temperature_2m_max"], label="1983", color='purple')

# Ajouter les titres et légendes
plt.title("Température maximale à 2m (par année)", fontsize=14)
plt.xlabel("day", fontsize=12)
plt.ylabel("Température maximale à 2m (°C)", fontsize=12)
plt.legend(title="Années", fontsize=10)  # Légende des séries
plt.grid(True)  # Ajout d'une grille pour une meilleure lecture

# Affichage du graphique
plt.show()