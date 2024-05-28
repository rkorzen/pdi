x = -10

if x > 0:
    print(x)
    print("wewntarz ifa")

if x > 0:
    print(x)
    print("wewntarz ifa")
    
print("na zewnatrz")
print("to już jest po wyrazeniu")


"""
jeżeli <warunek> to <blok kodu>

if (x > 0) {print(x)}

if (x > 0) {
   print(x);
}

print("to już jest po wyrazeniu")


"""


"""
jeżli <warun> to 
   <blok kodu>
w przeciwnym wypadku to
   <inny blok kodu>
"""


if x > 0:
    print(x ** 0.5)
else:
    print((-x) ** 0.5)   
    
    

"""
jeżli <warunek> to 
   <blok kodu>
jeżeli <inny warunek> to 
   <blok kodu 2>
jeżeli <inny warunek> to 
   <blok kodu 3>
jeżeli <inny warunek> to 
   <blok kodu 4>
w przeciwnym wypadku to
   <inny blok kodu>
"""


if x > 0:
    print(x ** 0.5)
elif x == 0:
    print(1)
else:
    print((-x) ** 0.5)   
    
    


if bool(0):
    print("warunek spełniony")


if 0:
    print("warunek spełniony")


# 0, "", 0.0, [], (), {} -> False

print(bool(0))

print(bool(100), bool("ala"), bool([1, 2]))


x = 1
if x == True:
    print("warunek spełniony w x jest wartość True")
    


x = 1
if x:
    print("warunek spełniony w x jest wartość True")
        
        

x = 1
if x is True:
    print("warunek spełniony w x jest wartość True")
    
    
print(id(True))

print(id(1 == 1))

print(id(2 > 1))

print(id(x))

x = 102

if x > 100 and x % 2 == 0:
    print("sdsdsd")
    
    
x = 10
y = 0

if x > 0 or x / y > 2:
    print("csdsd")


x = -1

if x < 0 and x / y > 2:
    print("csd234sdf3sd")


# sygnalizuje ze jest cos takiego jak structural patterns matching
x = 2
match x:
    case 1:
        print("opcja spełniona")
    case 2:
        print("xxxx")
        