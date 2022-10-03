# Számológép program
'''
print("Számológép\n")

a = int(input("Kérek egy számot: "))
b = int(input("Kérek egy másik számot: "))
muvelet = input("Kérek egy műveletet: ")

if muvelet == "+":
    print(a + b)
elif muvelet == "-":
    print(a - b)
elif muvelet == "*":
    print(a * b)
elif muvelet == "/":
    print(a / b)
else:
    print("Érvénytelen művelet!")

'''

bemenet = input("Kérem a számokat a műveleti jellel együtt (1 + 2):\t")

if "+" in bemenet:
    pos = bemenet.find("+")

    a = int(bemenet[:pos])
    b = int(bemenet[pos + 1:])
    print(a + b)

elif "-" in bemenet:
    pos = bemenet.find("-")

    a = int(bemenet[:pos])
    b = int(bemenet[pos + 1:])
    print(a - b)
    
elif "*" in bemenet:
    pos = bemenet.find("*")

    a = int(bemenet[:pos])
    b = int(bemenet[pos + 1:])
    print(a * b)

elif "/" in bemenet:
    pos = bemenet.find("/")

    a = int(bemenet[:pos])
    b = int(bemenet[pos + 1:])
    print(a / b)   

else:
    print("Érvénytelen/hiányzó művelet!")
    exit()