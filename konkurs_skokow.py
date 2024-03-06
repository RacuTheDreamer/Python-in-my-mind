import random

def policz_punkty_za_skok(odleglosc, wiatr, punkty_konstrukcyjne):
    punkty_skok = 60 + (odleglosc - punkty_konstrukcyjne) * 1.8  if odleglosc > punkty_konstrukcyjne else (
        60 - (punkty_konstrukcyjne - odleglosc) * 1.8 if odleglosc < punkty_konstrukcyjne else 60)
    
    suma_punktow = punkty_skok


    suma_punktow +=  wiatr
    suma_punktow = round(suma_punktow, 1)
    
    if suma_punktow < 0:
        suma_punktow = 0
    return suma_punktow

while True:

    punkty_konstrukcyjne = float(input("Podaj punkt konstrukcyjny: "))

    odleglosc1 = float(input("Podaj odległość skoku 1: "))
    odleglosc2 = float(input("Podaj odległość skoku 2: "))
    wiatr1 = float(input("Podaj siłę wiatru dla skoku 1: "))
    wiatr2 = float(input("Podaj siłę wiatru dla skoku 2: "))

    punkty_skok_1 = policz_punkty_za_skok(odleglosc1, wiatr1, punkty_konstrukcyjne)
    punkty_skok_2 = policz_punkty_za_skok(odleglosc2, wiatr2, punkty_konstrukcyjne)

    print(f"Punkty za skok 1: {punkty_skok_1}")
    print(f"Punkty za skok 2: {punkty_skok_2}")
    print(f"Suma punktów: {(punkty_skok_1 + punkty_skok_2)}")

    print("\nCzy chcesz powtórzyć operację?")
    print("1. Tak")
    wybor = input("Twój wybór: ")

    if wybor == "1":
        continue 
    else:
        break

        
