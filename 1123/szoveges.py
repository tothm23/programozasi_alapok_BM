nev = input("A teljes neved: ")
# print(nev[0:nev.index(" ")])
# print(nev[nev.index(" ") + 1:])

nevT = nev.split(" ")
# print(f"A vezetékneved: {nevT[0]}")
# print(f"A keresztneved: {nevT[1]}")

print(f"Vezetéknév: {nevT[0].capitalize()}")
for elem in nevT[1:]:
    if not elem[0].isupper():
        print(f"Keresztnév: {elem.capitalize()}")
    else:
        print(f"Keresztnév: {elem}")

javitva = []
javNev = ""
for elem in nevT:
    javitva.append(elem.capitalize())
    javNev += elem.capitalize() + " "

print(f"A javított név: {javNev}")