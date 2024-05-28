
# with open("data.txt") as f:
#     for line in f:
#         data = line.strip().split(",")
#         print(data)

import csv

with open("data.txt") as f:
    reader = csv.reader(f, delimiter=";", quotechar="'")
    for row in reader:
        print(row[2])

with open("data.txt") as f:
    reader = csv.DictReader(f, delimiter=";", quotechar="'")
    for row in reader:
        print(row["wynik"])


