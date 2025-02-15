from flask import Flask, render_template, request, jsonify
import os
import time
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.szpital
collection = db.pacjenci

def wyszukiwanie_pacjentow(zmienna):
    documents = collection.find({}, {'ID': 1})
    lista_id = []
    boolionIdPodstawowe = False

    for document in documents:
        ID = document.get('ID', 'Brak')
        _id = str(document.get('_id', 'Brak'))
        konto = {"ID": ID, "_id": _id}
        lista_id.append(konto)

    ID_Nowe = zmienna.get("ID")
    ID_Tajne_Nowe = zmienna.get("_id")

    for i in range(len(lista_id)):
        if lista_id[i].get("ID") == ID_Nowe:
            print(f"takie id istnieje: {ID_Nowe}")
            print(f"watosć boolion {boolionIdPodstawowe}")
            boolionIdPodstawowe = True
            return boolionIdPodstawowe

    if boolionIdPodstawowe == False:
        with open('static/dane_powszechny_spis_kont.json', 'r') as file:
            pacjenci = json.load(file)
            pacjenci.append(zmienna)

        with open('static/dane_powszechny_spis_kont.json', 'w') as file:
            json.dump(pacjenci, file)

        for pacjent in pacjenci:
            if collection.count_documents({"ID": pacjent["ID"]}) == 0:
                pacjent.update({
                    "Puls": [],
                    "CiśnienieKrwi": [],
                    "KonsumpcjaTlenu": [],
                    "PoziomSodu": [],
                    "PoziomPotasu": [],
                    "TemperaturaCiała": [],
                    "PoziomGlukozy": [],
                    "MorfologiaKrwi": [],
                    "Rentgen": [],
                    "Tomografia": [],
                    "SaturacjaTlenem": [],
                    "CzęstośćOddechu": [],
                    "AktualizacjaDziałania": []
                })
                collection.insert_one(pacjent)

        documents = collection.find({}, {'ID': 1, 'Imie': 1, 'Wiek': 1, 'Nazwisko': 1})
        lista_kont = []
        for document in documents:
            ID = document.get('ID', 'Brak')
            imie = document.get('Imie', 'Brak')
            wiek = document.get('Wiek', 'Brak')
            nazwisko = document.get('Nazwisko', 'Brak')
            _id = str(document.get('_id', 'Brak'))

            konto = {"ID": ID, "Imię": imie, "Wiek": wiek, "Nazwisko": nazwisko, "_id": _id}
            lista_kont.append(konto)
            lista_id.append(_id)

        with open('static/dane_o_kontach.json', 'w') as json_file:
            json.dump(lista_kont, json_file)
        return False

def usuwanie_Pacjentow(zmiennaID):
    ID = zmiennaID.get("ID")
    tejneIdSlownik = {"ID": f"{ID}"}
    print(f"usuwam: {ID}")

    with open('static/dane_powszechny_spis_kont.json', 'r') as file:
        pacjenci = json.load(file)
        usuwana = next((i for i, pacjent in enumerate(pacjenci) if int(pacjent.get("ID")) == ID), None)
        if usuwana is not None:
            pacjenci.pop(usuwana)

    with open('static/dane_powszechny_spis_kont.json', 'w') as file:
        json.dump(pacjenci, file)

    with open('static/dane_o_kontach.json', 'r') as file:
        pacjenci = json.load(file)
        usuwana = next((i for i, pacjent in enumerate(pacjenci) if int(pacjent.get("ID")) == ID), None)
        if usuwana is not None:
            pacjenci.pop(usuwana)

    with open('static/dane_o_kontach.json', 'w') as file:
        json.dump(pacjenci, file)

    collection.delete_one(tejneIdSlownik)

app = Flask(__name__)

@app.route('/')
def nauka_menu():
    return render_template('menu.html')

@app.route('/listaPacjenci/', methods=['GET', 'POST'])
def nauka():
    if request.method == 'POST':
        zmienna = request.get_json()
        with open('static/dane_o_ID_pacjenta.json', 'w') as json_file_Zmienna_listy:
            json.dump(zmienna, json_file_Zmienna_listy)

    return render_template('Panel_sterowaina_pacjenci.html')

@app.route('/listaPacjenci/nauka/<username>/')
def nauka_page(username):
    return render_template('nauka.html', username=username)

@app.route('/listaPacjenci/dodawaniePacjenta/', methods=['GET', 'POST'])
def nauka_dodawaine_pacjenta():
    if request.method == 'POST':
        zmienna = request.get_json()
        if wyszukiwanie_pacjentow(zmienna):
            return f"takie ID  {zmienna["ID"]} juz istnieje."  
        else:
            return "dodano"  

    return render_template('dodawaniePacjenta.html')  # Obsługa GET



@app.route('/listaPacjenci/usuwaniePacjenta/', methods=['GET', 'POST'])
def nauka_usuwanie_pacjenta():
    if request.method == 'POST':
        zmiennaID = request.get_json()
        usuwanie_Pacjentow(zmiennaID)

    return render_template('Panel_sterowaina_pacjenci.html')

if __name__ == '__main__':
    app.run(debug=True)
