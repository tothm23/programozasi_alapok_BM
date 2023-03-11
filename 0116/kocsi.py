class Autotip:
    
    def __init__(self, marka, tipus, nemzetiseg):
        self.marka = marka
        self.tipus = tipus
        self.nemzetiseg = nemzetiseg

    def nemzet(self):
        if self.nemzetiseg == "D":
            return "Német"
        elif self.nemzetiseg == "H":
            return "Magyar"
        elif self.nemzetiseg == "I":
            return "Olasz"
        else:
            return "Ismeretlen"

Lautok = []
for _ in range(3):
    marka = input("Márka: ")
    tipus = input("Típus: ")
    nemzetiseg = input("Felségjelzés (D, H, I): ")
    
    auto = Autotip(marka, tipus, nemzetiseg)
    Lautok.append(auto)

for elem in Lautok:
    print("A(z)", elem.marka, elem.tipus, "egy ", elem.nemzet(), "autó!")