import random
osztaly = [random.randint(160, 200) for x in range(27)]
print(osztaly)

print("1. feladat")
osszeg = 0
for elem in osztaly:
    osszeg += elem
print(f"Az osztály átlagmagassága: {round(float(osszeg) / len(osztaly), 2)} cm")

print("\n2. feladat")
print(f"A(z) {osztaly.index(max(osztaly)) + 1}. tanuló a legmagasabb")

print("\n3. feladat")
print(f"{max(osztaly) - min(osztaly)} cm különbség van a legmagasabb és a legalacsonyabb között")

print("\n4. feladat")
print(f"{round(osszeg / 100, 2)} m-es torony keletkezne")

print("\n5. feladat")
osztaly.append(182)
print("A tanuló felvéve")

print("\n6. feladat")
osztaly.sort()
print("A tornasor: ", end=" ")
for elem in osztaly:
    print(elem, end=", ")

print("\n\n7. feladat")
egyformak = False
i = 0
while i < len(osztaly) - 1:
    if osztaly[i] == osztaly[i + 1]:
        egyformak = True
        break
    i += 1

if egyformak:
    print("Vannak egyforma magasak az osztályban")
else:
    print("Nincsenek egyforma magasak az osztályban")