#%%
import random
import pandas as pd

from custom_modules.my_games import Dobbelsteen

#%% Definitie van de 'Dobbelsteen' class



#%%
mijn_dobbelsteen = Dobbelsteen("Rood", 20)
# %%
mijn_dobbelsteen.worpen
# %%
mijn_dobbelsteen.werp_dobbelsteen()

# %%
mijn_dobbelsteen.worpen
# %%
mijn_dobbelsteen.verwijder_worpen()
# %%
x = mijn_dobbelsteen.geef_worpen_weer()


# %%
personen_dict = {"namen": ['arie', 'jaap', 'dirk'],
                 "leeftijden": [20, 30, 40]}

#%%
df = pd.DataFrame(personen_dict)
# %%


# %%
list(mijn_dobbelsteen.worpen_dict.keys())
# %%
list(mijn_dobbelsteen.worpen_dict.values())
# %%
dobbelsteen_dict = {"worp_nr" : list(mijn_dobbelsteen.worpen_dict.keys()),
                    "worp": list(mijn_dobbelsteen.worpen_dict.values())}
# %%
df_worpen = pd.DataFrame(dobbelsteen_dict)
# %%
worp_nr_list = list(mijn_dobbelsteen.worpen_dict.keys())
worpen_list = list(mijn_dobbelsteen.worpen_dict.values())

#%%
df_dobbelsteen = pd.DataFrame({
                               "worp_nr" : worp_nr_list,
                               "worp": worpen_list
                           })




















# %%
