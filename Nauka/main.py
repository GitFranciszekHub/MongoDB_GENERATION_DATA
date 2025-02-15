#importy do tworzenia wykresu
import matplotlib.pyplot as plt
import time
#importy do połączenia mongoDB z pythonem 
from pymongo import MongoClient
from bson.objectid import ObjectId
#łączenie mongodb z pythonem, wybór kolekcji i bazy danych
from pprint import pprint
client = MongoClient('localhost', 27017)
db = client['szpital']
collection = db['pacjenci']
# aby zapisać JSON
import json



def pobieranieDanej():

    with open('static/dane_o_ID_pacjenta.json', 'r') as file:
        data = json.load(file)
    ID_tajne = data["ID_tajne"]
    print(ID_tajne)
    return ID_tajne



def wyszukiwanie_pacjentow(collection): 

        documents = collection.find({}, {'ID': 1,'Imie': 1, 'Wiek': 1, 'Nazwisko': 1})  
        lista_kont = []
        for document in documents:
            ID = document.get('ID', 'Brak')
            imie = document.get('Imie', 'Brak')
            wiek = document.get('Wiek', 'Brak')
            nazwisko = document.get('Nazwisko', 'Brak')
            _id = str(document.get('_id', 'Brak'))
    
            
            konto = {"ID":ID,"Imię": imie, "Wiek": wiek, "Nazwisko": nazwisko, "_id": _id}           
            lista_kont.append(konto)
            lista_id.append(_id)

        with open('static/dane_o_kontach.json', 'w') as json_file:
            json.dump(lista_kont, json_file)
            json_file.close()







            


def wyszukiwanie_wartosci():
    zmienna_id = f"{pobieranieDanej()}"
    document_id = ObjectId(zmienna_id)
    document = collection.find_one({'_id': document_id})
    for i in lista_id:
        if i != zmienna_id:
            print(f"{i} i {zmienna_id} Nie są sobie równe")
            
        elif i == zmienna_id:
            try:
                    ostatnia_czestosc_oddechu = sorted(document["CzęstośćOddechu"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_SaturacjaTlenem = sorted(document["SaturacjaTlenem"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_Puls = sorted(document["Puls"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_temperatura_ciala = sorted(document["TemperaturaCiała"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_poziom_potasu = sorted(document["PoziomPotasu"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_poziom_sodu = sorted(document["PoziomSodu"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_konsumpcja_tlenu = sorted(document["KonsumpcjaTlenu"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_cisnienie = sorted(document["CiśnienieKrwi"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_MorfologiaKrwi = sorted(document["MorfologiaKrwi"], key=lambda x: x['czas'], reverse=True)[0]['wartość']
                    ostatnia_Hemoglobina=sorted(document["MorfologiaKrwi"], key=lambda x: x['czas'], reverse=True)[0]['wartość']["Hemoglobina"] 
                    ostatnia_Erytrocyty=sorted(document["MorfologiaKrwi"], key=lambda x: x['czas'], reverse=True)[0]['wartość']["Erytrocyty"] 
                    ostatnia_Leukocyty=sorted(document["MorfologiaKrwi"], key=lambda x: x['czas'], reverse=True)[0]['wartość']["Leukocyty"] 
                    ostatnia_Plytki_krwi=sorted(document["MorfologiaKrwi"], key=lambda x: x['czas'], reverse=True)[0]['wartość']["Plytki_krwi"] 


                    zapisz_do_json(ostatnia_czestosc_oddechu, ostatnia_SaturacjaTlenem, ostatnia_Puls,  
                                ostatnia_temperatura_ciala, ostatnia_poziom_potasu, ostatnia_poziom_sodu, ostatnia_konsumpcja_tlenu,ostatnia_cisnienie,ostatnia_MorfologiaKrwi,
                                ostatnia_Hemoglobina,ostatnia_Erytrocyty,ostatnia_Leukocyty,ostatnia_Plytki_krwi)

                    tworzenieGrafu(ostatnia_czestosc_oddechu, ostatnia_SaturacjaTlenem, ostatnia_Puls, ostatnia_temperatura_ciala, 
                                ostatnia_poziom_potasu, ostatnia_poziom_sodu, ostatnia_konsumpcja_tlenu
                                ,ostatnia_Hemoglobina,ostatnia_Erytrocyty,ostatnia_Leukocyty,ostatnia_Plytki_krwi)
                    break
            except :
                print("Brak pacjentow lub coś poszło nie tak")
        else:
            print("Coś poszło nie tak")
            time.sleep(1)
    time.sleep(1)










def zapisz_do_json(ostatnia_czestosc_oddechu, ostatnia_SaturacjaTlenem, ostatnia_Puls, ostatnia_temperatura_ciala, 
                   ostatnia_poziom_potasu, ostatnia_poziom_sodu, ostatnia_konsumpcja_tlenu,ostatnia_cisnienie,ostatnia_MorfologiaKrwi
                   ,ostatnia_Hemoglobina,ostatnia_Erytrocyty,ostatnia_Leukocyty,ostatnia_Plytki_krwi):
    dane = {
        "CzestoscOddechu": ostatnia_czestosc_oddechu,
        "SaturacjaTlenem": ostatnia_SaturacjaTlenem,
        "Puls": ostatnia_Puls,
        "CisnienieKrwi": ostatnia_cisnienie,
        "TemperaturaCiala": ostatnia_temperatura_ciala,
        "PoziomPotasu": ostatnia_poziom_potasu,
        "PoziomSodu": ostatnia_poziom_sodu,
        "KonsumpcjaTlenu": ostatnia_konsumpcja_tlenu,
        "ostatnia_MorfologiaKrwi":ostatnia_MorfologiaKrwi,
        "ostatnia_Hemoglobina":ostatnia_Hemoglobina,
        "ostatnia_Erytrocyty":ostatnia_Erytrocyty,
        "ostatnia_Leukocyty":ostatnia_Leukocyty,
        "ostatnia_Plytki_krwi":ostatnia_Plytki_krwi,
    }
    with open('static/dane.json', 'w') as json_file:
        json.dump(dane, json_file)


def tworzenieGrafu(ostatnia_czestosc_oddechu, ostatnia_SaturacjaTlenem, ostatnia_Puls, ostatnia_temperatura_ciala, ostatnia_poziom_potasu, sod, ostatnia_konsumpcja_tlenu
                   ,ostatnia_Hemoglobina,ostatnia_Erytrocyty,ostatnia_Leukocyty,ostatnia_Plytki_krwi):
    

    wybrana_wartosc_pop = 0
    wybrana_wartosc_len = 6

    lista_wartosci = [
        lista_tworzenie_wartosc_CzestoscOddechu,
        lista_tworzenie_SaturacjaTlenem,
        lista_tworzenie_puls,
        lista_tworzenie_temperatura_ciala,
        lista_tworzenie_poziom_potasu,
        lista_tworzenie_poziom_sodu,
        lista_tworzenie_konsumpcja_tlenu,
        lista_ostatnia_Hemoglobina,
        lista_tworzenie_ostatnia_Erytrocyty,
        lista_tworzenie_ostatnia_Leukocyty,
        lista_tworzenie_ostatnia_Plytki_krwi
    ]

    ostatnie_wartosci = [
        ostatnia_czestosc_oddechu,
        ostatnia_SaturacjaTlenem,
        ostatnia_Puls,
        ostatnia_temperatura_ciala,
        ostatnia_poziom_potasu,
        sod,
        ostatnia_konsumpcja_tlenu,
        ostatnia_Hemoglobina,
        ostatnia_Erytrocyty,
        ostatnia_Leukocyty,
        ostatnia_Plytki_krwi
    ]


    for i in lista_wartosci:
        if len(i) == wybrana_wartosc_len:
            i.pop(wybrana_wartosc_pop)


    for lista, wartosc in zip(lista_wartosci, ostatnie_wartosci):
        lista.append(wartosc)




    # Wykresy
    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_wartosc_CzestoscOddechu)
    ax.set_xlim(0, 5)
    ax.set_ylim(10, 22)
    ax.set_title("Częstość Oddechu")
    plt.savefig('static/wartosc_CzestoscOddechu.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_SaturacjaTlenem)
    ax.set_xlim(0, 5)
    ax.set_ylim(95, 100)
    ax.set_title("Saturacja Tlenem")
    plt.savefig('static/SaturacjaTlenem.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_puls)
    ax.set_xlim(0, 5)
    ax.set_ylim(60, 100)
    ax.set_title("Puls")
    plt.savefig('static/Puls.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_temperatura_ciala)
    ax.set_xlim(0, 5)
    ax.set_ylim(36, 38)
    ax.set_title("Temperatura Ciała")
    plt.savefig('static/TemperaturaCiala.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_poziom_potasu)
    ax.set_xlim(0, 5)
    ax.set_ylim(3.5, 5)
    ax.set_title("Poziom Potasu")
    plt.savefig('static/PoziomPotasu.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_poziom_sodu)
    ax.set_xlim(0, 5)
    ax.set_ylim(135, 145)
    ax.set_title("Poziom Sodu")
    plt.savefig('static/PoziomSodu.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_konsumpcja_tlenu)
    ax.set_xlim(0, 5)
    ax.set_ylim(90, 100)
    ax.set_title("Konsumpcja Tlenu")
    plt.savefig('static/KonsumpcjaTlenu.png')
    plt.close(fig)  # Zamknięcie figury


    fig, ax = plt.subplots()
    ax.plot(lista_ostatnia_Hemoglobina)
    ax.set_xlim(0, 5)
    ax.set_ylim(12, 18)
    ax.set_title("Hemoglobina")
    plt.savefig('static/Hemoglobina.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_ostatnia_Erytrocyty)
    ax.set_xlim(0, 5)
    ax.set_ylim(4.5, 6.0)
    ax.set_title("Poziom Erytrocyty")
    plt.savefig('static/Erytrocyty.png')
    plt.close(fig)  # Zamknięcie figury

    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_ostatnia_Leukocyty)
    ax.set_xlim(0, 5)
    ax.set_ylim(4.0, 11.0)
    ax.set_title("Leukocyty")
    plt.savefig('static/Leukocyty.png')
    plt.close(fig)  # Zamknięcie figury


    fig, ax = plt.subplots()
    ax.plot(lista_tworzenie_ostatnia_Plytki_krwi)
    ax.set_xlim(0, 5)
    ax.set_ylim(150, 400)
    ax.set_title("Plytki krwi")
    plt.savefig('static/Plytki_krwi.png')
    plt.close(fig)  # Zamknięcie figury


    time.sleep(1)



lista_tworzenie_ostatnia_Plytki_krwi = []
lista_tworzenie_ostatnia_Leukocyty = []
lista_tworzenie_ostatnia_Erytrocyty = []
lista_ostatnia_Hemoglobina = []

lista_tworzenie_cisnienie = []
lista_tworzenie_wartosc_CzestoscOddechu = []
lista_tworzenie_SaturacjaTlenem = []
lista_tworzenie_puls = []
lista_tworzenie_temperatura_ciala = []
lista_tworzenie_poziom_potasu = []
lista_tworzenie_poziom_sodu = []
lista_tworzenie_konsumpcja_tlenu = []
lista_id=[]
time.sleep(1)
# Pętla pobierająca dane co 4 sekundy
while True:
    wyszukiwanie_pacjentow(collection)
    wyszukiwanie_wartosci()
