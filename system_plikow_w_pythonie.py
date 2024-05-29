import os
import pathlib
# from pathlib import Path
directory = "dane"
#
# for item in os.listdir(directory):
#     print(item)
#


for root, dirs, files in os.walk(directory):
    print(f"Zawartość {root}:")
    for file in files:
        print(f"  Plik: {file}")
    for dir in dirs:
        print(f"  podkatalog: {dir}")


print(__builtins__.dir())

p = pathlib.Path("dane")

for item in p.rglob("*"):
    print(item)



for root, dirs, files in p.walk():
    print(f"Zawartość {root}:")
    for file in files:
        print(f"  Plik: {file}")
    for dir in dirs:
        print(f"  podkatalog: {dir}")


print(os.path.exists("dane/tata.txt"))

with open("dane/tata.txt", "w") as f:
    f.write("xxx")

folder_path = p / "dane"

folder_path.mkdir(exist_ok=True)

plik_path = p / "dane" / "tata2.txt"
plik_path.touch()
# with plik_path.open("w") as f:
#     f.write("something")

# os.remove("dane/tata.txt")


