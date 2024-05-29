import re

text = "Zadzwon pod numer 780 232 123  kod zamowienia 123123245356546 780 232 124"

pattern = r"\d{3} \d{3} \d{3}"

match = re.search(pattern, text)

print(match.group())


match = re.findall(pattern, text)

print(match)

text = "123 123 123"

print(re.match(pattern, text))


dane = """
Jan, Kowalski, 30, Warszawa
Anna, Nowak; 25, Kraków
"""

pattern = r"(\w+), (\w+), (\d+), (\w+)"

for line in dane.splitlines():
    match = re.match(pattern, line)
    if match:
        imie, nazwisko, wiek, miasto = match.groups()

        print(imie, nazwisko, wiek, miasto)

