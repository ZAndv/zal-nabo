[![demo](https://github.com/ZAndv/zal-nabo/actions/workflows/demo.yml/badge.svg)](https://github.com/ZAndv/zal-nabo/actions/workflows/demo.yml)

Kalkulator CLI (pełne)

 Opis projektu
Projekt przedstawia kalkulator działający w trybie CLI (Command Line Interface).
Umożliwia wykonywanie podstawowych i rozszerzonych operacji matematycznych.

 Funkcjonalności 
 Dodawanie
 Odejmowanie
 Mnożenie
 Dzielenie
 Potęgowanie
 Pierwiastkowanie
 Historia obliczeń

 Struktura projektu
 main.py – główny plik programu (menu CLI)
 operations.py – operacje matematyczne
 history.py – zapis i odczyt historii
 utils.py – obsługa błędów
 tests.py – testy funkcji
Uruchom
Vladyslav Vinichenko 1 – operacje matematyczne
Oleksandr  Boiarov 2 – interfejs CLI
Maksym Podzolkin 3 – historia obliczeń
Hlib Kvasnevskyi 4 – obsługa błędów
Andrii Kuzynskyi 5 – testowanie

Instrukcja uruchomienia: 

1.)docker pull olaspa/calc-cli:latest

2.)docker run -it olaspa/calc-cli:latest

Link do obrazu Docker: https://hub.docker.com/repository/docker/olaspa/calc-cli/general
