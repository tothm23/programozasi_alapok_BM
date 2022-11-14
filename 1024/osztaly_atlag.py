import random

osztalyzatok = [random.randint(1, 5) for i in range(5)]
osszeg = sum(osztalyzatok)

#osszeg = 0
#for elem in osztalyzatok:
#    osszeg += elem

print(f"{osztalyzatok}")
print(f"Az osztályzatok átlaga: {osszeg / len(osztalyzatok)}\n")

osztalyzatok.sort()
print(f"{osztalyzatok}")

osztalyzatok.reverse()
print(f"{osztalyzatok}")

keresett = int(input("\nKeresett jegy: "))
if keresett in osztalyzatok:
    print("Van ilyen elem")
else:
    print("Nincs ilyen elem")