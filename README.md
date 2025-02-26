# MongoDB_GENERATION_DATA
Jest to zainspirowana GE Healthcare platforma, mająca na celu formatowanie danych pobieranych z urządzeń medycznych Iot, tak aby użytkownicy mogli mieć dostęp do informacji niezależnie od miejsca, w którym się znajdują.

<hr>
 1. Język programowania kodu źródłowego.<br>
 2. Cel i zadania programu i aplikacji.<br>
 3. Uruchamianie programu i aplikacji.
<hr>

Kod źródłowy jest napisany przy użyciu języka programowania Python wersji Python 3.12.9.
Biblioteki, moduły które zostały użyte w projekcie:<br>pymongo<br>matplotlib
   


 
Funkcjonalności:
-Pobieranie danych w czasie rzeczywistym
-Generowanie wykresów w czasie rzeczywistym
-Segregowanie danych
-Dodawanie i usuwanie urządzeń 
-Symulacja danych dla każdego z urządzeń
-przechowywanie informacji o pacjentach 

Technologie:
-Python 3.12.9
-MongoDB
-Matplotlib
-flask
-json


Uruchomienie:
Należy wpisać w konsole: 
-python dane_kliniczne_pacjentow.py, aby zacząć generewać dane i wysyłać do MongoDB.
-python main.py, aby zacząć pobierać dane z Mongodb, zapisywać je  w odpowiednich json i tworzyć wykresy matplotlib.
-python appN.py, aby uruchomić serwer flask i kierować danymi.


LINK DO INSPIRACJI:
https://www.mongodb.com/blog/post/connected-devices-ge-healthcare-uses-mongodb-manage-iot-device-lifecycle
