import random
import time

szam_gep = random.randint(1, 100)
szam_tipp = None

probalkozasok = 1
print(szam_gep)

kezdes = time.time()
while szam_tipp != szam_gep:
    try:
        szam_tipp = int(input("A tip: "))
    except ValueError:
        print("A beírt érték nem szám!")
        probalkozasok += 1
        continue

    if szam_tipp > szam_gep:
        print("A gondolt szám kisebb!")
    else:
        print("A gondolt szám nagyobb!")
    
    
    if szam_tipp == szam_gep:
        zaras = time.time()
        print("Gratulálok! Eltaláltad!")
        print(f"Próbálkozásaid: {probalkozasok}")
        print(f"Eltelt idő: {round(zaras - kezdes, 1)} mp")
    else:
        probalkozasok += 1