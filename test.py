import json

sciezka = "C:\\Users\\w67263\\Desktop\\"

market = {
            "na_sklepie": 
            {

            "owoce": ["jablko", "sliwka","gruszka","morele"],
            "warzywa": ["ziemniaki", "marchewki","kapusta"],
            "pieczywo": ["buleczki", "chleb","bagietka"],
            "nabiał": ["sery", "mleko"],
            "mięso": ["kurczak", "wieprzowina","baranina","dziczyzna"]
 
            }

        }

with open(sciezka="plik_json3.json", encoding="utf-8", mode="w") as plik:
    json.dump(market, plik)

with open(sciezka="plik_json3.json", encoding="utf-8", mode="r") as plik:
    dane = plik.read

#print(dane)
    
    dane_json = json.loads(dane)
    print(dane_json)
    print(dane_json['kontakt'].keys())
    for klucz in dane_json['kontakt'].keys():
        print(klucz, " : ", (dane_json['kontakt'])[klucz])
