lista = []
be = float(input("Kérek egy + számot: "))

for i in range(3):
    while be < 0:
        print("A szám - !")
        be = float(input("Kérek egy másik + számot: "))
    
    lista.append(be)
print(lista)