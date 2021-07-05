#%%
namen_lijst = ['Arie', 'Jaap', 'Dirk']

#%%
print(namen_lijst[0])
print(namen_lijst[1])
print(namen_lijst[2])
# %%
for i in namen_lijst:
    print(i)
# %%
namen_lijst

# %%
for key, value in enumerate(namen_lijst):
    print(key)
    print(value)
    print("-"*20)

# %%
for naam in namen_lijst:
    print(naam)

# %%
personen_dict = {}

namen_lijst = ['Arie', 'Jaap', 'Dirk']
leeftijden_lijst = [20, 30, 40]

for key, value in enumerate(namen_lijst):
    personen_dict[f'persoon_{str(key)}'] = {'naam' : value,
                                            'leeftijd': leeftijden_lijst[key],
                                            'huisdieren': [{'dier' : 'kat', 
                                                            'leeftijd': 8}, 'hond', 'cavia']}
    

# %%
