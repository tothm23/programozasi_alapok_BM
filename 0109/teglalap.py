def kerulet(a, b):
    return 2 * (a + b)

def terulet(a, b):
    return a * b

def main():
    a = int(input("a = "))
    b = int(input("b = "))

    print("\nK =", kerulet(a, b))
    print("T =", terulet(a, b))

if __name__ == "__main__":
    main()