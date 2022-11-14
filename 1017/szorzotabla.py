import random

pont = 0
print("Szorzótábla")
feladat = int(input("Hány feladatra van időd? "))

for i in range(feladat):
    szam1 = random.randint(1, 10)
    szam2 = random.randint(1, 10)

    eredmeny = szam1 * szam2
    valasz = int(input(f"{i + 1}. Feladat: {szam1} * {szam2} = "))
    
    if valasz == eredmeny:
        print("Helyes!")
        pont += 1

    else:
        print("Helytelen")

print(f"Statisztika: {pont} / {feladat} ({round((pont / feladat) * 100, 2)}%)")