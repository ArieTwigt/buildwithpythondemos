#%% 
from haas_funs.calc_funs import calc_circle
from haas_funs.string_funs import hebrewize

#%%
x = calc_circle(10)

# %%
naam = hebrewize("Jan")
# %%
print(naam)

#%%
lordify = lambda x: f"Lord. {x}"
# %%
lordify("arie")
# %%
lordify = lambda x, y: f"Lord. {x} {y}"

#%%
lordify("arie", "twigt")
# %%
lordify = lambda x: f"Lord. {x}"
namen_lijst = ['Arie', 'Jaap', "Dirk's"]

#%%
lord_namen_lijst = [lordify(naam) for naam in namen_lijst]












# %%
namen_lijst = ['Arie', 'Jaap', 'Dirk']


#%%
def groet_namen(lijst):
    num_names = 0
    while num_names <= len(lijst):
        yield f"Hallo {lijst[num_names]}"
        num_names += 1
        
    
# %% maak generator aan
namen_gen = groet_namen(namen_lijst)
# %%
next(namen_gen)

#%%















# %%
from datetime import date, datetime, timedelta


#%%
datum = date(2021, 6, 24)

# %%
date_str = "2021-06-24"
date_date = datetime.strptime(date_str, "%Y-%m-%d")

# %%
