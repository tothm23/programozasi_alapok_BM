faktorialis = input("A faktoriális: ") #5!

elvalaszto = faktorialis.index("!") # lekéri a ! helyét
szam = int(faktorialis[:elvalaszto]) # levágja a ! jelet
print(f"szam: {faktorialis[:elvalaszto]}")

"""
osszeg = 1
fakt = int(input("faktoriális = "))

for i in range(1, fakt + 1):
    osszeg *= i    

print(osszeg)
"""