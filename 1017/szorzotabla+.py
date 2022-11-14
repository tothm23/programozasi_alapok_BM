import random

szam1 = random.randint(1, 10)
szam2 = random.randint(1, 10)

eredmeny = szam1 * szam2
valasz = None
hiba = 0

print("Szorzótábla")
while valasz != "" or int(valasz) != eredmeny:
    valasz = int(input(f"{szam1} * {szam2} = "))
    
    if valasz == eredmeny:
        print(f"Helyes! Hibáid száma: {hiba}")
        break

    else:
        print("Helytelen")

    hiba += 1