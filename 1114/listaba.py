Lszamok = []

be = input("Kérek egy számot: ")
while be != "":
    
    # Ha nem üres, továbbenged
    """
    be = int(be)
    if be in Lszamok:
        print("Ilyen elem már van!")
    else:
        Lszamok.append(be)
    be = input("Kérek egy számot: ")
    """

    be = int(be)
    while be in Lszamok:
        print("Ilyen elem már van!")
        be = input("Kérek egy számot: ")

    if be != "":
        Lszamok.append(int(be))
        be = input("Kérek egy számot: ")

print(Lszamok)

"""
for i in range(len(Lszamok) - 1):
    if Lszamok[i] + 1 == Lszamok[i + 1]:
        egymas_utani = True
        break
"""
i = 0
egymas_utani = False
while i < len(Lszamok) - 1 and Lszamok[i] + 1 == Lszamok[i + 1]:
    i += 1

if i > 0:
    egymas_utani = True

"""
while i != len(Lszamok) - 1:
    if Lszamok[i] + 1 == Lszamok[i + 1]:
        van = True
    if i == len(Lszamok):
        break
"""

print(f"Egymás utáni számok: {egymas_utani}")