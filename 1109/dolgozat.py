import random

fo = int(input("Hány fős az osztály? "))
jegyek = [random.randint(1, 5) for x in range(fo)]
print(jegyek)

# Feladatok
print("\n1. feladat")

osszeg = 0
for elem in jegyek:
    osszeg += elem

print(f"Az osztályátlag: {round(osszeg / len(jegyek), 2)}")

print("\n2. feladat")
print("Statisztika")

print(f"5: {jegyek.count(5)}")
print(f"4: {jegyek.count(4)}")
print(f"3: {jegyek.count(3)}")
print(f"2: {jegyek.count(2)}")
print(f"1: {jegyek.count(1)}")

# tárolja a megszámolt jegyeket
stat = [jegyek.count(5), jegyek.count(4), jegyek.count(3), jegyek.count(2), jegyek.count(1) ]
jegyek = [5, 4, 3, 2, 1]

print("\n3. feladat")
print(stat)

# 
idx = stat.count(max(stat))
print(f"A legtöbb jegy: {jegyek[idx]}")