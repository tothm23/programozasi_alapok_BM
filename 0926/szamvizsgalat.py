szam1 = int(input("Első szám: "))
szam2 = int(input("Második szám: "))

"""
if szam1 > szam2:
    print("Az 1. szám a nagyobb")
elif szam1 < szam2:
    print("A 2. szám a nagyobb")
else:
    print("A két szám egyenlő.")
"""

print("Az 1. szám a nagyobb") if szam1 > szam2 else print("A 2. szám a nagyobb") if szam1 < szam2 else print("A két szám egyenlő.")