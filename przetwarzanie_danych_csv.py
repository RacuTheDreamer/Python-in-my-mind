import pandas as pd 
import os
import numpy as np

path_input = r'C:\\Users\\w67263\\Downloads\\baza_gus1.xlsx' #sciezka wejsciowa odeczytu

if os.path.exists(path_input):
    df = pd.read_excel(path_input)
    print(np.array(df))
    print()
    
    df["suma"] = df['a2021'] + df['a2022'] + df['a2023']
    df['srednia'] = df['suma'] / (len(df.columns)-3)
    
   # print(("describe"), df.describe)
   
    path_output = r'C:\\Users\\w67263\\Downloads\\baza_gus2.xlsx' #sciezka wyjsciowa zapisu

    df.to_excel(path_output)

    print(df.iloc[6:9,2:5]) #zakres wierszy od 0,   zakres kolumn od 0
    print()
    print(df.at[8, 'srednia']) # 'srednia' dla wiersza 8
    print()
    print(df.loc[df['srednia'] > 75])  #srednia dla wierszy 'srednia' wiekszych niz 75

    
else:
    print("Ścieżka do pliku nie istnieje.")
