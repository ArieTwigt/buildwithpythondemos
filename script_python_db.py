#%%
import pandas as pd
import sqlite3

#%% 
con = sqlite3.connect("autos.db")

#%%
query = """
        SELECT * 
        FROM jaarmaand
        WHERE jaar_maand = ?
        """

#%%
x = 20191
df_autos = pd.read_sql(query, params=(x,), con=con)
# %%
