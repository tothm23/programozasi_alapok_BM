# Szerkeszthető-e a háromszög?
def szerkesztheto(a, b, c):
    return "szerkeszthető" if a + b > c and a + c > b and b + c > a else "nem szerkeszthető"
    
def main():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print(f"A háromszög {szerkesztheto(a, b, c)}.")

if __name__ == "__main__":
    main()
