# MongoDB_GENERATION_DATA
Jest to zainspirowana GE Healthcare platforma, mająca na celu formatowanie danych pobieranych z urządzeń medycznych Iot, tak aby użytkownicy mogli mieć dostęp do informacji niezależnie od miejsca, w którym się znajdują.<br>
<hr>
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
<b>2. Projekt jest podzielony na trzy części.</b><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;1.Program symulujący dane medyczne  (plik dane_kliniczne_pacjentow.py).<br>
&nbsp;&nbsp;&nbsp;&nbsp;2.Aplikacjia webowa (plik appN.py).<br>
&nbsp;&nbsp;&nbsp;&nbsp;3.Program generujący wykresy medyczne (plik main.py).<br><br>
<b>Zadaniama programu symulującego danymi:</b><br><br>
-Generowanie danych o wartościach zbliżonych do rzeczywistych.<br><br>
-Generowanie danych dla każdego pacjenta.<br><br>
-Zapisywanie wygenerowanych danych.<br><br>
-Wysyłanie wygenerowanych danych do pliku JSON w celu przekazania ich do programu generującego wykresy medyczne.<br><br>
<b>Zadaniami aplikacji webowej:</b><br>
-Zapewnienie czytelności poprzez stworzenie odpowiednio przystosowanej warstwy wizualnej (HTML, CSS). <br><br>
-Umożliwienie użytkownikowi wygodnego poruszania się po aplikacji i jej komponentach.<br><br>
-Umożliwienie użytkownikowi zapoznania się z danymi, odbieranie ich w czasie rzeczywistym oraz filtrowanie.<br><br>
-Pobieranie od użytkownika danych pacjentów i wysyłanie ich do programu symulującego dane.<br><br>
-Informowanie za pomocą pliku JSON programu tworzącego wykresy, dla którego pacjenta powinien on tworzyć wykresy, oraz przekazywanie danych numerycznych.<br>
<b>Zadaniami progrmu generującego wykresy medyczne:</b><br><br>
-Pobieranie  w czasie rzeczywistym danych (dla pacjenta wybranego przez użytkowika w aplikacji webowej)z bazy danych MongoDb.<br><br>
-generowanie przy użyciu matplotlib wykresów w czasie rzeczywistym.
-przesyłanie do aplikacji webowej danych numerycznych dla wybranego pacjenta i wykresów w czasie rzeczywistym 



<b>Uruchomienie:</b>
1. Przejdź na oficjalną stronę MongoDB: https://www.mongodb.com/try/download/community.
Kieruj się instrukcjami na stronie <br>
2. Uruchamianie symulowania danych.<br>
 otworzyć nowy wiersz poleceń,<br - przejść do ścieżki projektu np. ‘C:\Pulpit\jobmeup\project’, <br- zakładając, że użytkownik posiada zainstalowanego Pythona z 
wersją   3.12.9 lub nowszą: 
&nbsp;&nbsp;&nbsp;&nbsp;> wpisać ‘python dane_kliniczne_pacjentow.py’. 
&nbsp;&nbsp;&nbsp;&nbsp;> w razie braku Pythona, należy odwiedzić główną stronę 
https://www.python.org/ pobrać wspomianą wersję i dodać 
Python do ścieżki środowiskowej PATH.<br>
3. Uruchamianie tworzenia wykresów danych.<br>
 otworzyć nowy wiersz poleceń,<br> - przejść do ścieżki projektu np. ‘C:\Pulpit\jobmeup\project’,<br> - zakładając, że użytkownik posiada zainstalowanego Pythona z 
wersją   3.12.9 lub nowszą: 
&nbsp;&nbsp;&nbsp;&nbsp;> wpisać ‘python main.py’. 
&nbsp;&nbsp;&nbsp;&nbsp;> w razie braku Pythona, należy odwiedzić główną stronę 
https://www.python.org/ pobrać wspomianą wersję i dodać 
Python do ścieżki środowiskowej PATH.
4.Uruchamianie Aplikacji webowej.<br>
 otworzyć nowy wiersz poleceń,<br> - przejść do ścieżki projektu np. ‘C:\Pulpit\jobmeup\project’,<br> - zakładając, że użytkownik posiada zainstalowanego Pythona z 
wersją   3.12.9 lub nowszą: 
&nbsp;&nbsp;&nbsp;&nbsp;> wpisać ‘python appN.py’. 
&nbsp;&nbsp;&nbsp;&nbsp;> w razie braku Pythona, należy odwiedzić główną stronę 
https://www.python.org/ pobrać wspomianą wersję i dodać 
Python do ścieżki środowiskowej PATH.

