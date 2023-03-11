import os

def szamit(eletkor):
    """
    Meghatározza, hogy vehet-e cigit
    """

    if eletkor >= 18:
        return True
    else:
        return False

def main():
    nev = input("A neved: ")

    while nev != "":
        
        try:
            eletkorod = int(input("Az életkorod: "))

            if szamit(eletkorod):
                print(f"{nev}, kaphat cigarettát!")
            else:
                print(f"{nev}, nem kaphat cigarettát!")
        except ValueError:
            os._exit(0)
        nev = input("A neved: ")
    
    
if __name__ == "__main__":
    main()