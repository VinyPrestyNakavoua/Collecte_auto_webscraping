import pandas as pd
import glob
 
# list all csv files only
csv_files = ["objects_info_1-100.csv", "objects_info_100-200.csv", "objects_info_200-300.csv", "objects_info_300-1000.csv"]

df_csv_append = pd.DataFrame()
 
# append the CSV files
for file in csv_files:
    df = pd.read_csv(file)
    df_csv_append = df_csv_append.append(df, ignore_index=True)


print(df_csv_append)