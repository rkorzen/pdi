# napisy

print("to jest napis")
print('to tez jest napis')

print("\nx\ny\n")
print(r"\nx\ny\n")
print("\\nx\\ny\\n")
print("a\tb")
# print("\a")

print("Ala ma \r kota")

# napisy wielolinijkowe
print("""
x
y
""")

print(
''' x '''
)


# typy liczbowe

# int - liczby calkowite

print(1 + 200203560560 -1000)
print(-1)

print(1_000_99_999)

# bool - typ boolowski
# True - 1, False - 0

print(1 + True)
print("porownanie True z 1", 1 == True)
# print(1 / False)

# float - liczby zmiennoprzecinkowe

print(1.1)
print(1.2e-234)
print(1.2e10)

print(0.1 + 0.1 + 0.1)
# http://pywaw.org/105/#talk-float-wszystko-o-co-baliscie-sie-zapytac

print(float("inf"))
print(float("-inf"))
print(float("nan"))

print(1.8e307)
print( 1 == 1)
print(float("nan") == float("nan"))

# complex - liczby zespolone

print(1 + 3j)

# operatory arytmetyczne

1 + 1
1 - 1
1 * 3
print(1 / 2)
1 // 2
1 % 2

2 ** 4

print(1 + 1.1)
# print("1" + 1)

# operatory dzialajace na napis

print("10" * 10)
print("10" + "20")

# print("10" - "1")

# bool - typ logiczny

print(1 > 2)

# operatory logiczne
"""
and
or
not
"""
# operatory porownania

1 == 2
1 > 2
1 < 3
1 >= 2
2 <= 2
2 != 3

# operatory przypisania

x = 1
x += 1 # x = x + 1
x -= 1

x = x * 1 # x *= 2






# inne typy

bytes
bytearray
frozenset

print(type(101))


# zamiana typów, konwersja, rzutowanie

print(float(10))

print(float("10"))

print(int("10", base=2))
print(int("c0ffee", base=16))

print(0b1111)
print(0o1111)
print(0x1111)


print(
bin(100),
oct(100),
hex(100),
)























