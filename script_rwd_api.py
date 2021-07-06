#%%
import requests
import json
import pandas as pd
import sqlite3

#%%
url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?$select=handelsbenaming, datum_tenaamstelling, count(datum_tenaamstelling)&merk=TESLA&$group=handelsbenaming, datum_tenaamstelling&$where=datum_tenaamstelling IS NOT NULL AND datum_tenaamstelling >=  20190131&$order=datum_tenaamstelling ASC"

#%%
resp = requests.get(url)

#%%
resp_list = json.loads(resp.text)

#%%
autos_dict = {
    "handelsbenaming": [],
    "datum_tenaamstelling": [],
    "aantal": [],
}

#%%
for key, value in enumerate(resp_list):
    autos_dict["handelsbenaming"].append(value['handelsbenaming'])
    autos_dict["datum_tenaamstelling"].append(value['datum_tenaamstelling'])
    autos_dict["aantal"].append(value['count_datum_tenaamstelling'])


#%%
df_autos = pd.DataFrame(autos_dict)

#%%
df_autos.dtypes

#%% 
# datatype aanpassen
df_autos['aantal'] = df_autos['aantal'].astype(float) 
df_autos['datum_tenaamstelling'] = pd.to_datetime(df_autos['datum_tenaamstelling'], format="%Y-%m-%d")
df_autos['jaar']  = df_autos['datum_tenaamstelling'].dt.year
df_autos['maand'] = df_autos['datum_tenaamstelling'].dt.month
df_autos['jaar_maand'] = df_autos['jaar'].astype(str) + df_autos['maand'].astype(str)

#%%
# kolommen selecteren 
columns  = ['jaar_maand', 'aantal']
df_autos[columns]
# data aggregeren
df_autos_aggregated = df_autos[columns].groupby('jaar_maand').sum().reset_index()

#%%
con = sqlite3.connect("autos.db")   


df_autos_aggregated.to_sql("jaarmaand", con=con, if_exists="append")


# %%
print("Done")