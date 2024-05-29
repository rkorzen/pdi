from datetime import datetime

class Czlowiek:

    def __init__(self, imie, rok_ur):
        self.imie = imie
        self.rok_ur = rok_ur

    @property
    def wiek(self):
        now = datetime.now()
        return now.year - self.rok_ur

    def __repr__(self):
        return f"Czlowiek({self.wiek})"



class MixinRejestracjaPracy:

    def rejestruj_godziny(self, godziny):
        self.godziny += godziny

class Pracownik(Czlowiek, MixinRejestracjaPracy):

    def __init__(self, imie, rok_ur, stawka):
        super().__init__(imie, rok_ur)
        self.stawka = stawka
        self.godziny = 0

    def __repr__(self):
        return f"Pracownik(rok_ur:{self.wiek} stawka: {self.stawka})"


p = Czlowiek("Rafał", 1980)
pracownik = Pracownik("Wojtek", 1991, 200)
pracownik.rejestruj_godziny(10)
pracownik.rejestruj_godziny(12)
print(pracownik.godziny)

