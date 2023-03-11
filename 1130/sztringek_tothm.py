text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print("\n1. feladat")
print(f"A szöveg {len(text)} karakterből áll")

print("\n2. feladat")
szavak = text.split(" ")
print(f"A szöveg {len(szavak)} szóból áll")

print("\n3. feladat")
mondatok = text.split(".")
print(f"A szöveg {len(mondatok) - 1} mondatból áll")

print("\n4. feladat")
szamok = []
karakterek = ".,:;'\" "
for szo in szavak:
    szam = ""
    for betu in szo:
        if not betu.isalpha() and betu not in karakterek:
            szam += betu
            #print(betu)
        
    #print(szam)
    if szam != "":
        szamok.append(int(szam))
    #print()

print("A számok: ", end="")
for elem in szamok:
    print(elem, end=", ")

print("\n\n5. feladat")
# Ha nincs benne szám, akkor hibát dob
print(f"A legkisebb és a legnagyobb szám közötti különbség: {max(szamok) - min(szamok)}")