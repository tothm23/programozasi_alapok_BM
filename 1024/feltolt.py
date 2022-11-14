import random

szamok = []

# feltöltés
for i in range(5):
    szamok.append(int(input("adj meg egy számot: ")))
    szamok.append(random.randint(1, 10))

# feltöltés végjelig
"""
szam = None
while szam != 0:
    szam = int(input("Kéek egy számot: "))
    szamok.append(szam)
"""

# feldolgozás
print(szamok)