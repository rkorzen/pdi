try:
    f = open("formatowanie_napisow.py", encoding="utf-8")
    for i, line in enumerate(f, start=1):

        print(i, line, end="")
finally:
    print("zamykam połączenie")
    f.close()


# context manager
with open("formatowanie_napisow.py", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(i, line, end="")

