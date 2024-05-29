import json

dane = {
  "obiekty": [
    {"typ": "triangle", "area":  123},
    {"typ": "square", "area":  55}
  ]
}


json_dane = json.dumps(dane)
print(json_dane, type(json_dane))

raw_data = '{"obiekty": [{"typ": "triangle", "area": 123}, {"typ": "square", "area": 55}]}'
d = json.loads(raw_data)

print(d, type(d))

with open("dane.json") as f:
    d = json.load(f)
    print(d, type(d))


with open("xxxx.json", "w") as f:
    napisy = ["ąę", "ala", "kot"]
    json.dump(napisy, f)


with open("xxxx.json") as f:
    print(f.read())

with open("xxxx.json") as f:
    d = json.load(f)
    print(d, type(d))