# Dolgozat kiértékelése
def kiertekel(pont):
    jegy = 0
    if 91 <= pont <= 100:
        jegy = 5
    elif 81 <= pont <= 90:
        jegy = 4
    elif 61 <= pont <= 80:
        jegy = 3
    elif 41 <= pont <= 60:
        jegy = 2
    elif 0 <= pont <= 40:
        jegy = 1
    else:
        jegy = -1 

    return jegy

def main():

    pont = float(input("Az elért pont: "))
    if kiertekel(pont) == -1:
        print("Érvénytelen pont!")
    else:
        print(f"Érdemjegy: {kiertekel(pont)}")

if __name__ == "__main__":
    main()