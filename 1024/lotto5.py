import random

szamok = []
szam = random.randint(1, 90)

for i in range(5):

    #if szam in szamok:
    #    szam = random.randint(1, 90)
    
    while szam in szamok:
        szam = random.randint(1, 90)
    szamok.append(szam)

print(f"A heti nyerőszámok: {szamok}")