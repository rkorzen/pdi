import csv
import kantor

with open("waluty_do_kupienia.csv") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        kantor.calculate(row["kod"], int(row["pln"]))