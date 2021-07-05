import pandas as pd
import random

class Dobbelsteen:
    
    # 1. default parameters
    aantal_vlakken = 6
    volume = None
    worpen = []
    worpen_dict = {}
    
    
    # 2. initial parameters/attributes
    def __init__(self, kleur, diameter):
        self.kleur    = kleur
        self.diameter = diameter
        self.volume = diameter * diameter * diameter
        
        print("🎊🎉 Gefeliciteerd, je hebt een dobbelsteen aangemaakt. Have fun!")
        pass
    
    # 3. Methods aanmaken
    def pas_vlakken_aan(self, nieuwe_vlakken):
        self.aantal_vlakken = nieuwe_vlakken
        
    def voeg_vlakken_toe(self, toevoegen_vlakken):
        self.aantal_vlakken += toevoegen_vlakken
        
      
    def werp_dobbelsteen(self):
        max_worp = self.aantal_vlakken
        worp = random.randint(1, max_worp)
        print("Minimum is 1")
        print(f"Maxiumum is {max_worp}")
        print(f"🎲 Je hebt {worp} gegooid!")
        self.worpen.append(worp)
        
        # toevoegen aan worpen_dict
        worp_nr = len(self.worpen) 
        self.worpen_dict[f'{worp_nr}'] = worp
        
        # create the worpen table
        self.create_worpen_tabel()
        
        
    def geef_worp_waarde(self, worp_nr):
        if worp_nr <= len(self.worpen_dict):
            x = self.worpen_dict[f"{worp_nr}"]
            print(x)
        else:
            minimum_waarde  = range(len(self.worpen_dict))[0] 
            maxiumum_waarde = range(len(self.worpen_dict))[1]
            print(f"Worp {worp_nr} is niet beschikbaar. \nKies een waarde tussen de {minimum_waarde} en {maxiumum_waarde}")
        

    def geef_worpen_weer(self, manier="kaal"):
        '''
        
        Geeft historische worpen weer
        
        
        etc.
        '''
        
        if manier == "uitgebreid":
            for worp in self.worpen:
                print(f"=======\n🎲 {worp}\n=======")
        else:
            print(self.worpen)
            return self.worpen
            
    
    def create_worpen_tabel(self):
        # haal de worp_nr en worpen uit de 'self.worpen_dict'
        worp_nr_list = list(self.worpen_dict.keys())
        worpen_list  = list(self.worpen_dict.values())

        # maak een DataFrame aan
        df_dobbelsteen = pd.DataFrame({
                                       "worp_nr" : worp_nr_list,
                                       "worp": worpen_list
                                   })
        
        # geeft de DataFrame weer
        self.worpen_table = df_dobbelsteen
        return df_dobbelsteen
    
    def verwijder_worpen(self):
        self.worpen = []     
        self.worpen_dict = {}
        self.worpen_table = pd.DataFrame()
        print("Worpen zijn verwijderd")
        print(self.worpen)
        
        
    def get_worp_statistics(self):
        print(self.worpen_table['worp'].describe())
        
    
    def get_total_sum_worpen(self):
        return self.worpen_table['worp'].sum() 
    
    
    def export_csv(self, naam):
        self.worpen_table.to_csv(f"{naam}.csv", sep="|", index=False)
        print(f"✅ '{naam}.csv' succesfully exported")
        
    
    def display_worpen(self):
        self.worpen_table.plot.bar(x="worp_nr", y="worp")
        
    pass