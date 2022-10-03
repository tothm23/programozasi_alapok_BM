"""
    Háromszög
    @author tothm
"""

def kiertekel(a, b, c):
    """
    if (a + b > c) and (a + c > b) and (b + c > a): 
        print("Szerkeszthető")
    else:
        print("Nem szerkeszthető meg")
    """

    print("Szerkeszthető") if (a + b > c) and (a + c > b) and (b + c > a) else print("Nem szerkeszthető meg")

def main():

    print("Szerkeszthető a háromszög?")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    kiertekel(a, b, c)

if __name__ == "__main__":
    main()
