from dataclasses import dataclass


class ObliczeniaOld:

    def __init__(self, a, b, wynik):
        self.a = a
        self.b = b
        self.wynik = wynik

    def __repr__(self):
        return f"Obliczenia(a={self.a}, b={self.b}, wynik={self.wynik})"


# DTO
@dataclass
class Obliczenia:

    a: int
    b: int
    wynik: int


o = Obliczenia(1, 2, 3)
o2 = ObliczeniaOld(1, 2, 3)

print(o)
print(o2)


class Foo:
    x = "atrybut klasowy"

    def __init__(self, y):
        self.y = y


f1 = Foo(10)
f2 = Foo(20)

print(f1.x, f2.x)

Foo.x = "XXXXX"

print(f1.x, f2.x)

f1.x = "YYYY"

print(f1.x, f2.x)


