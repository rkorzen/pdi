"""
Modul kalkulatora
"""

import requests
import sys


def wypisz_kody_walut():
    url = "http://api.nbp.pl/api/exchangerates/tables/C/today?format=json"
    response = requests.get(url)
    print("Dostępne waluty:")
    for w in response.json()[0]["rates"]:
        print( w["code"], w["currency"])

def calculate(waluta, kwota):
    """Przelicza kwote zakupu waluty w oparciu o wartosc waluta (kod waluty) i kwota"""
    url = "http://api.nbp.pl/api/exchangerates/tables/C/today?format=json"
    response = requests.get(url)
    dane = response.json()
    for w in dane[0]["rates"]:
        if w["code"] == waluta:
            cena = w["ask"] * kwota
            print(f"Za {kwota} PLN kupisz {cena} {waluta}")


def main():
    if len(sys.argv) == 1:

        print("Witaj w Kantorze!")
        wypisz_kody_walut()
        co = input("Jaką walutę chcesz wymienić (wpisz kod waluty): ")
        ile = int(input("Ile chcesz wymienić PLN (wpisz kwotę): "))

    elif len(sys.argv) == 3:
        co = sys.argv[1]
        ile = int(sys.argv[2])
    else:
        print("Niepoprawne użycie - podaj walutę i cene lub wywołaj program bez argumentów")
        exit()

    calculate(co, ile)



# print(dir())
# print(__doc__)
# print("wartosc __name__", __name__)

if __name__ == "__main__":
    main()
