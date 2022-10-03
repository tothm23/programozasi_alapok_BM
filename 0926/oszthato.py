# A beolvasott szám osztható 3-mal vagy 7-tel?

szam = int(input("Kérem a számot: "))

if szam % 3 == 0 and szam % 7 == 0:
    print(f"A(z) {szam} osztható 3-mal és 7-tel")
else:
    print(f"A(z) {szam} egyikkel sem osztható")