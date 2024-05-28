# while

"""
dopoki <warunek> rob 
   <blok kodu>


"""

x = 0
while x < 10:
    print(x)
    x += 1

"""
powtarzaj w nieskonczonosc
    <blok kodu>



powtarzaj w nieskonczonosc
    <blok kodu>
    przerwij

"""

x = 0
while True:
    print("haha")
    x += 1
    if x == 10:
         break
# for


i, j = 0, 0

while i < 10:
    while j < 10:
        print( i * j)
        j += 1
    i += 1