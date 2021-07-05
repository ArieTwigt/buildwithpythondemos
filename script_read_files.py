#%%
import json

#%%
with open("configs.json") as file:
    configs = file.read()
    
#%% 
type(configs)

# %%
config_dict = json.loads(configs)

# %%

# %%
int("ddd")
# %%
