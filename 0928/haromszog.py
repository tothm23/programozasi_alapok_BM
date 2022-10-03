"""
    Feladat:
    Egy derékszögő háromszög két oldalából kiszámítja az átfogót

    Tesztadatok:
    a = 2
    b = 1
    c = 2,2360679774997896964091736687313
    c = 2,24
"""

def szamol(a, b):
    
    # math.sqrt(5) = 5**(0.5)
    return  (a * a + b * b)**(0.5)
    
def main():

    a = float(input("a = "))
    b = float(input("b = "))

    c = szamol(a, b)
    print(f"c = {round(c, 2)}")

if __name__ == "__main__":
    main()
