import random

szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot: "))


if szam1 > szam2:
    for i in range(3):
        print(f"A véletlen szám: {random.randint(szam2, szam1)}")
else:
    for i in range(3):
        print(f"A véletlen szám: {random.randint(szam1, szam2)}")
        
"""
try:
    for i in range(3):
        print(f"A véletlen szám: {random.randint(szam1, szam2)}")
except ValueError:
    print("A 2. szám nagyobb, mint az 1. szám!")
"""
