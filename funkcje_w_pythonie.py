
# definicja
def nazwa_funkcji():  # sygnatura
    print("Hello")


nazwa_funkcji()  # wywołanie

#
# def suma(a, b):
#     print(a + b)

def suma(a, *args, b=0, **kwargs):
    print("args=", args)
    wynik = a + b
    for x in args:
        wynik += x
    return wynik

suma(1, 2)
suma(1)
suma(20)



wynik = suma(1, 2)
print(wynik)
print(wynik * 10)

suma(1, 2)
suma(1, 2, 3, 4, 5,6 ,7, 8, 89,34,56 , 7, c=123)


# suma(1, 2, 3 )

a, *b = 1, 2, 4, 5, 6, 7
print(a, b)


print("xx", suma(a, *b))  # suma(1, 2, 4, 5, 6, 7)
print("yy", suma(1, 2, 4, 5, 6, 7))