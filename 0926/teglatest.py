# Ez a program kiszámolja a téglatest felszínét, térfogatát

# Kiszámolja a felszínt
def felszin(a, b, c):
    return 2 * (a * b + a * c + b * c)

# Kiszámolja a térfogatot
def terfogat(a, b, c):
    return a * b * c

def main():

    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))

        print(f"A = {felszin(a, b, c)} cm\u00b2")
        print(f"V = {terfogat(a, b, c)} cm\u00b2")
    except ValueError:
        print("Érvénytelen érték!")

if __name__ == "__main__":
    main()