szamok = [20, 3, 11, 78, 90]

db = 0
for szam in szamok:
    if szam % 2 == 0:
        db += 1
        # print(szam, end=" ")
print(f"Páros számok száma: {db} db")