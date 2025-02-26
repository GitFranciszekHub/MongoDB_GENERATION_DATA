# MongoDB_GENERATION_DATA
Jest to zainspirowana GE Healthcare platforma, mająca na celu formatowanie danych pobieranych z urządzeń medycznych Iot, tak aby użytkownicy mogli mieć dostęp do informacji niezależnie od miejsca, w którym się znajdują.<br>
LINK DO INSPIRACJI:
https://www.mongodb.com/blog/post/connected-devices-ge-healthcare-uses-mongodb-manage-iot-device-lifecycle
<hr>
 1. Język programowania kodu źródłowego.<br>
 2. Cel i zadania programu i aplikacji.<br>
 3. Uruchamianie programu i aplikacji.
<hr>

<b>1. Kod źródłowy</b> został napisany w języku programowania Python w wersji 3.12.9.
Biblioteki i moduły użyte w projekcie: pymongo 4.10.1, matplotlib 3.10.0, Flask 3.0.3 oraz kilka innych.<br>
Aplikacja webowa jest również połączona z wieloma plikami HTML, CSS i JavaScript.
<br><br>
<b>2. Projekt jest podzielony na trzy części.<b><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;1.Program symulujący dane medyczne  (plik dane_kliniczne_pacjentow.py).<br>
&nbsp;&nbsp;&nbsp;&nbsp;2.Aplikacjia webowa (plik appN.py).<br>
&nbsp;&nbsp;&nbsp;&nbsp;3.Program generujący wykresy medyczne (plik main.py).<br><br>
<b>Zadaniami aplikacji webowej:<b><br>
-Zapewnienie czytelności poprzez stworzenie odpowiednio przystosowanej warstwy wizualnej (HTML, CSS). <br><br>
-Umożliwienie użytkownikowi wygodnego poruszania się po aplikacji i jej komponentach.<br><br>
-Umożliwienie użytkownikowi zapoznania się z danymi, odbieranie ich w czasie rzeczywistym oraz filtrowanie.<br><br>
-Pobieranie od użytkownika danych pacjentów i wysyłanie ich do programu symulującego dane.<br><br>
-Informowanie za pomocą pliku JSON programu tworzącego wykresy, dla którego pacjenta powinien on tworzyć wykresy, oraz przekazywanie danych numerycznych.



Funkcjonalności:
-Pobieranie danych w czasie rzeczywistym
-Generowanie wykresów w czasie rzeczywistym
-Segregowanie danych
-Dodawanie i usuwanie urządzeń 
-Symulacja danych dla każdego z urządzeń
-przechowywanie informacji o pacjentach 




Uruchomienie:
Należy wpisać w konsole: 
-python dane_kliniczne_pacjentow.py, aby zacząć generewać dane i wysyłać do MongoDB.
-python main.py, aby zacząć pobierać dane z Mongodb, zapisywać je  w odpowiednich json i tworzyć wykresy matplotlib.
-python appN.py, aby uruchomić serwer flask i kierować danymi.



