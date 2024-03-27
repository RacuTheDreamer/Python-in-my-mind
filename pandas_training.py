import pandas as pd 
import os
import matplotlib.pyplot as plt

path_input = r'C:\\Users\\w67263\\Desktop\\ramus\\czesc.xlsx' #sciezka wejsciowa odczytu

if os.path.exists(path_input):
    df = pd.read_excel(path_input, engine='openpyxl')

    def zaliczenie(punkty):
        if punkty > 15:
            return "zal"
        else:
            return "nzal"

    def suma(row):
        return (row["Kolos1"] + row["Kolos2"] + row["Kolos0"])

    def srednia(row):
        return round((row["Kolos1"] + row["Kolos2"] + row["Kolos0"]) / 3, 2)
    
    df["Srednia"] = df.apply(srednia, axis=1) #axis=0 dla każdej kolumny, a axis=1 dla każdego wiersza
    df["Suma"] = df.apply(suma, axis=1)
    df["Wynik"] = df["Suma"].apply(zaliczenie)
    df[['Imie', 'Nazwisko']] = df['Dane personalne'].str.split(' ', expand=True)
    
    print(df)

    df_zal = df.loc[df['Wynik'] == 'zal']
    
    print()
    print(df_zal)

    plt.figure(figsize=(10, 6))
    plt.hist(df['Srednia'], bins=10, color='orange', edgecolor='black')
    plt.title('Rozkład średnich ocen')
    plt.xlabel('Średnia ocena')
    plt.ylabel('Liczba studentów')
    plt.grid(True)
    plt.show()

else:
    print("Ścieżka do pliku nie istnieje.")
