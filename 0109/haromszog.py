def szerkesztheto(a, b, c):
    valasz = False
    if a < b + c and b < a + c and c < a + b:
        valasz = True
    
    return valasz

def kerulet(a, b, c):
    return a + b + c

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if szerkesztheto(a, b, c):
    print(f"Szerkeszthető, K = {kerulet(a, b, c)}")
else:
    print("Nem szerkeszthető")