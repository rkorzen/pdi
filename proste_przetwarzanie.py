import csv

class Triangle:

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.validate()

    def validate(self):
        if self.a + self.b < self.c:
            raise ValueError(f"Ta trójka boków {self.a}, {self.b}, {self.c} nie tworzy trójkąta")

    def dzialanie(self):
        print(self.a - self.b + self.c)

    def inne_dzialanie(self):
        print(self.a - self.b - self.c)

# def dzialanie(row):
#     print(int(row["a"]) - int(row["b"]) + int(row["wynik"]))
#
# def inne_dzialanie(row):
#     print(int(row["a"]) + int(row["b"]) - int(row["wynik"]))

def przetwarzaj(kolekcja):
    for row in kolekcja:
        try:
            t = Triangle(row["a"], row["b"], row["wynik"])
            # dzialanie(row)
            # inne_dzialanie(row)
            t.dzialanie()
            t.inne_dzialanie()
        except Exception as e:
            print(f"Błąd w wierszu: {row}", e)



dane = [{"a": 10,"b": 20, "wynik": 30}]

with open("data.txt") as f:
    reader = csv.DictReader(f, delimiter=";", quotechar="'")
    przetwarzaj(reader)


przetwarzaj(dane)
