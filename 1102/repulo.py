import random

eredmenyek = [random.randint(0, 9) for x in range(20)]

print("1. feladat")
for i in eredmenyek:
    print(i, end="")

print("\n\n2. feladat")
print(f"A legmagasabb pont értéke: {max(eredmenyek)}")

print("\n3. feladat")
legkisebb = eredmenyek[0]
legnagyobb = eredmenyek[0]

for elem in eredmenyek:
    if elem != 0 and legkisebb > elem:
        legkisebb = elem
    if elem != 0 and legnagyobb < elem:
        legnagyobb = elem

print(f"A legalacsonyabb és legmagasabb hegy közötti különbség: {legnagyobb - legkisebb}")

print("\n4. feladat")
szarazfold = 0
viz = 0
for i in eredmenyek:
    if i == 0:
        viz += 1
    else:
        szarazfold += 1

if szarazfold > viz:
    print("Szárazföldből található több")
elif szarazfold < viz:
    print("Vízből található több")
else:
    print("Mindkettőből ugyananyi található")