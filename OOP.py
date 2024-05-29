
class Kwadrat:

    def __init__(self, bok=1):
        self.bok = bok

    @property
    def bok(self):
        return self._bok

    @bok.setter
    def bok(self, value):
        if value < 0:
            raise ValueError("Bok nie może być mniejszy od zera")

        self._bok = value

    @property  # property - atrybut dynamiczny
    def pole(self):
        return self.bok ** 2

    @pole.setter
    def pole(self, value):
        if value < 0:
            raise ValueError("Pole nie może być ujemne")
        self.bok = value ** 0.5

    def puchnij(self):
        self.bok = self.bok * 2

    def __gt__(self, other):
        return self.bok > other.bok

    def __eq__(self, other):
        return self.bok == other.bok

    def __ge__(self, other):
        return self.bok >= other.bok

    def __mul__(self, other):
        if isinstance(other, int):
            return Kwadrat(self.bok * other)
        elif isinstance(other, Kwadrat):
            return Kwadrat(self.bok * other.bok)
    def __rmul__(self, other):
        return Kwadrat(self.bok * other)

    # def __str__(self):
    #     return f"Kwadrat({self.bok})"
    def __repr__(self):
        return f"Kwadrat({self.bok})"

kw1 = Kwadrat(5)
# kw3 = Kwadrat(5)
kw2 = Kwadrat(4)
# block x
# print(kw1 > kw2)
# print(kw1 < kw2)
# print(kw1 == kw2)
# print(kw1 == kw3)
# print(kw1 != kw2)
# print(kw1 >= kw2)
# print(kw1 <= kw2)

# print("bok przed", kw2.bok)
# r = kw2 * 2
# print(r)
# print(kw1)
# print("bok po", kw2.bok)
# end block
# print([kw1, kw2, kw3, r])

print(kw1 * kw2)

# print(10 * kw1)