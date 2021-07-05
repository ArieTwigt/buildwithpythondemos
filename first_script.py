#%%
import pandas
# %%
"arie".capitalize()
# %%
"arie".__contains__("rie")
# %%
bestanden_lijst = ["/map_1/bestand_arie/",
 "/map_1/bestand_1/",
 "/map_2/bestand_8/",
 "/map_4/bestand_arie/",
 "/map_2/bestand_7/",
 "/map_9/bestand_arie/"
 ]

#%%
filter_lijst = [x for x in bestanden_lijst if x.__contains__("arie")]


# %%
filter_lijst = []
for x in bestanden_lijst:
    if x.__contains__("arie"):
        filter_lijst.append(x)
    else:
        pass


# %%
namen_lijst = ['Arie', 'Henk', 'Floris']
leeftijden  = [20, 30, 40]
# %%
personen_dict = dict(zip(namen_lijst, leeftijden))
personen_dict

# %%
personen_dict.keys()
# %%
personen_dict_2 = {}
personen_dict_2['namen'] = namen_lijst
personen_dict_2['leeftijden'] = leeftijden

# %%
import pandas as pd

personen_df = pd.DataFrame(personen_dict_2)
personen_df['woonplaasts'] = ['Enschede', 'Leiden', 'Amsterdam']
personen_df
# %%
personen_df.to_csv("personen.csv", sep=";", index=False)
# %%
personen_dict
# %%
personen_dict['Dirk']
# %%
from collections import defaultdict

personen_dict_3 = defaultdict(lambda: 'Onbekend')

personen_dict_3['Arie'] = 20

# %%
with open('params.json') as file:
    config = file.read()
# %%
config
# %%
import json
# %%
config_dict = json.loads(config)
# %%
from dotenv import load_dotenv

load_dotenv()

#%%
import os

os.environ.get('PASS')

# %%
personen_dict = {}
personen_dict['Arie'] =  31
personen_dict['Bas']  = 20
# %%
personen_dict.keys()
# %%
personen_dict['Jaap']


# %%
from collections import defaultdict

personen_dict = defaultdict(lambda: 'Leeftijd onbekend')


personen_dict['Arie'] =  31
personen_dict['Bas']  = 20
# %%
personen_dict.keys()
# %%
personen_dict['Marrie']
# %%
