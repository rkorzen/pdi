"""
input
while
with open ...

Pobierz od użytkownika jakies dane i zapisz je do pliku w formie wierszy

python zadanie_1.py

W kazdym momenecie mozesz wpisac q by zakonczyc
Podaj arg a: 1
Podaj arg b: 2

Podaj arg a: 3
Podaj arg b: 5

Podaj arg a: 4
Podaj arg b: q

Dziekuje zapisalem dane w dane.txt

a, b, wynik
1, 2, 3
3, 5, 8
"""


with open("data.txt", "a") as f:
    f.write(f"a, b, wynik\n")
    print("W kazdym momenecie mozesz wpisac q by zakonczyc")
    while True:
        a = input("Podaj arg a: ")

        if a == "q":
            break
        b = input("Podaj arg b: ")

        if b == "q":
            break

        print()
        result = int(a) + int(b)
        f.write(f"{a}, {b}, {result}\n")
