import sys

n = None
try:
    n = int(input("n = "))
except ValueError:
    print("Nem számot adtál meg!")
    sys.exit()

osszeg = 0

for i in range(1, n, 1):
    
    # Összeadja a négyzetszámokat
    osszeg += i * i

    # Négyzetre emel
    i * i

# Kiírja az átlagukat
print(osszeg / n)