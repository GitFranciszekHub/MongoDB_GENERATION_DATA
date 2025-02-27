
import random
from datetime import datetime
import time
import pytz
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.szpital
kolekcja_pacjentow = db.pacjenci

def aktualizacjaBazyPacjentow():

    with open('static/dane_powszechny_spis_kont.json', 'r') as file:
            pacjenci = json.load(file)


    for pacjent in pacjenci:
        if kolekcja_pacjentow.count_documents({"ID": pacjent["ID"]}) == 0:
            pacjent["Puls"] = []
            pacjent["CiśnienieKrwi"] = []
            pacjent["KonsumpcjaTlenu"] = []
            pacjent["PoziomSodu"] = []
            pacjent["PoziomPotasu"] = []
            pacjent["TemperaturaCiała"] = []
            pacjent["PoziomGlukozy"] = []
            pacjent["MorfologiaKrwi"] = []
            pacjent["Rentgen"] = []
            pacjent["Tomografia"] = []
            pacjent["SaturacjaTlenem"] = []
            pacjent["CzęstośćOddechu"] = []
            pacjent["AktualizacjaDziałania"] = []
            kolekcja_pacjentow.insert_one(pacjent)
    return pacjenci


def generuj_dane_pacjenta():
    
    while True:
        for pacjent in aktualizacjaBazyPacjentow():
            id_pacjenta = pacjent["ID"]
            czas = datetime.now()

            puls = random.randint(60, 100)
            cisnienie_skurczowe = random.randint(110, 140)
            cisnienie_rozkurczowe = random.randint(70, 90)
            cisnienie = f"{cisnienie_skurczowe}/{cisnienie_rozkurczowe}"
            konsumpcja_tlenu = random.randint(90, 100)
            poziom_sodu = round(random.uniform(135, 145), 2) 
            poziom_potasu = round(random.uniform(3.5, 5.0), 2) 
            temperatura_ciala = round(random.uniform(36.5, 37.5), 1) 
            poziom_glukozy = round(random.uniform(70, 140), 2) 
            saturacja_tlenem = round(random.uniform(95, 100), 1) #
            czestosc_oddechu = round(random.uniform(12, 20)) #

            morfologia_krwi = {
                "Hemoglobina": round(random.uniform(12, 18), 2), 
                "Erytrocyty": round(random.uniform(4.5, 6.0), 2), 
                "Leukocyty": round(random.uniform(4.0, 11.0), 2), 
                "Plytki_krwi": round(random.uniform(150, 400), 2) 
            }

            rentgen = "Rentgen-" + id_pacjenta
            tomografia = "Tomografia-" + id_pacjenta
                               

            dane = {
                "ID": id_pacjenta,
                "czas": czas,
                "puls": puls,
                "cisnienie_krwi": cisnienie,
                "konsumpcja_tlenu": konsumpcja_tlenu,
                "poziom_sodu": poziom_sodu,
                "poziom_potasu": poziom_potasu,
                "temperatura_ciala": temperatura_ciala,
                "poziom_glukozy": poziom_glukozy,
                "morfologia_krwi": morfologia_krwi,
                "rentgen": rentgen,
                "tomografia": tomografia,
                "saturacja_tlenem": saturacja_tlenem,
                "czestosc_oddechu": czestosc_oddechu
            }


            kolekcja_pacjentow.update_one(
                {"ID": id_pacjenta},
                {"$push": {
                    "Puls": {"czas": czas, "wartość": puls},
                    "CiśnienieKrwi": {"czas": czas, "wartość": cisnienie},
                    "KonsumpcjaTlenu": {"czas": czas, "wartość": konsumpcja_tlenu},
                    "PoziomSodu": {"czas": czas, "wartość": poziom_sodu},
                    "PoziomPotasu": {"czas": czas, "wartość": poziom_potasu},
                    "TemperaturaCiała": {"czas": czas, "wartość": temperatura_ciala},
                    "PoziomGlukozy": {"czas": czas, "wartość": poziom_glukozy},
                    "MorfologiaKrwi": {"czas": czas, "wartość": morfologia_krwi},
                    "Rentgen": {"czas": czas, "wartość": rentgen},
                    "Tomografia": {"czas": czas, "wartość": tomografia},
                    "SaturacjaTlenem": {"czas": czas, "wartość": saturacja_tlenem},
                    "CzęstośćOddechu": {"czas": czas, "wartość": czestosc_oddechu}
                }}
            )
            print(f"Aktualizowano dane dla pacjenta {id_pacjenta} w czasie {czas}")

        time.sleep(8)

generuj_dane_pacjenta()