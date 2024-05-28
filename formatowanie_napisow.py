x1 = "Ala"
y1 = "kota"
z1 = 10

x2 = "Staś"
y2 = "rower"
z2 = 21

szablon = x1 + " ma " + y1
print(szablon)

szablon2 = "%s(%.2f) ma %s"

print(szablon2 % (x2, z2, y2))

szablon3a = "{}({:.2f}) ma {}"

print(szablon3a.format(x2, z2, y2))
szablon3b = "{imie:>20}({wiek:^7.2f}) ma {obiekt:^40}"
print(szablon3b)
print(szablon3b.format(imie=x1, wiek=z1, obiekt=y1))



text = f"{x2:>20}({z2:^7.2f}) ma {y2:^40}"
print(text)
