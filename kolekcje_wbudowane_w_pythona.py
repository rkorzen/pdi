# napis - jest niemutowalny
#       #0123456
napis = "XXXXYXX"

print(napis[2])

# napis[100]

print(napis[-3])

print(napis[1:5])  # slicing

print(napis[1:5:2])  # slicing

print("abcdef"[::-1])

# napis[1] = "D"

print(id(napis))

napis += "1"
print(id(napis))
print(napis)


# tupla - niemutowalna

print(tuple(napis))
krotka = (1, 2, 3, "napis", 1.2, (1,23), 1.2)

print(krotka[-1])

# krotka[-1] = 10

# lista - list - mutowalna

print(krotka)
lista = list(krotka)
print(lista)

print(lista[-1])
print(id(lista))
lista[-1] = 10
print(id(lista))
print(lista)


print([x for x in dir(krotka) if not x.startswith("__")])
print([x for x in dir(lista) if not x.startswith("__")])


print(krotka.count(1.2))
# print(help(krotka.count))
# print(help(krotka.count(1.2)))
print(help(krotka.index))
print(krotka.index(1.2))


lista.insert(0, "Ania")
print(lista)

lista.append("Kot")
print(lista)

help(lista.insert)

# zbior = set

lista.append(1.2)
print(lista)
zbior = set(lista)
print(zbior)

print({1, 2, 3, 1, 2, 3})
# print({[1,2], 3})

print(hash((1, 2, 3)))
# print(hash((1, 2, [3])))


print(set([1, 2,3, 1, 2, 3, 41, 2, 1,2 ,34 ,467 ,]))
print(set("AGCTAGCTAGCT"))


A = {1, 2, 3}
B = {2, 3, 4}

print(A | B)
print(A & B)
print(A - B)

print(A ^ B)

C = {3, 4}

print(C.issubset(B))
print(B.issuperset(C))

for el in B:
    print(el)

print(3 in C)
# slownik - dict

slownik = {"a": 1, "b": 2}

slownik["a"]

print(slownik.get("c"))
print(slownik.get("c", 100))


# podsumowanie

tuple, list, set, dict, str

# dodatkowo:
frozenset, bytearray, bytes

print(bytearray(b"zazolc gesla jazn")) # ASCII

# b"zażólć gęlą jaźń"


print("zażólć gęlą jaźń".encode())
print("zażólć gęlą jaźń".encode("utf-8-sig"))
print("zażólć gęlą jaźń".encode("CP1250"))

dane = b'za\xbf\xf3l\xe6 g\xeal\xb9 ja\x9f\xf1'

print(dane.decode("CP1250"))

print(b'\xef\xbb\xbfza\xc5\xbc\xc3\xb3l\xc4\x87 g\xc4\x99l\xc4\x85 ja\xc5\xba\xc5\x84'.decode())

# unicode