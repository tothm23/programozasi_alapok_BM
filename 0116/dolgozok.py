import random
szamok = [random.randint(0, 100) for elem in range(10)]

with open("szamok.txt", mode="w", encoding="utf-8") as fajl:
    for elem in szamok:
        print(elem, file=fajl)

db = 0
osszeg = 0
with open("szamok.txt", mode="r", encoding="utf-8") as fajl:
    for elem in fajl:
        elem = elem.strip()
        db += 1
        osszeg += int(elem)
    
print(f"{fajl.name} létrehozva!")
print(f"Átlag: {round(osszeg / db, 2)}")