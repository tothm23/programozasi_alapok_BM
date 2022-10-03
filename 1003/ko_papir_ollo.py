import random


# saját verzió
elemek = [ "kő", "papír", "olló"]

gep_veletlen = random.randint(0, len(elemek))
gep = elemek[gep_veletlen]
sajat = input("Kő, papír vagy olló? ")

if sajat.lower() == elemek[gep_veletlen]:
    print(f"Döntetlen! ({gep} : {sajat})")
elif elemek[gep_veletlen] == "kő" and sajat == "papír" or \
    elemek[gep_veletlen] == "papír" and sajat == "olló" or \
    elemek[gep_veletlen] == "olló" and sajat == "kő":
    print(f"User győzött! ({gep} : {sajat})")
else:
    print(f"Döntetlen! ({gep} : {sajat})")


"""
    # órai verzió
gepmutat = random.randint(0, 2) #0-kő, 1- papír, 2-olló
usermutat = int(input("Kő (0), papír (1), olló (2): "))

if gepmutat == usermutat:
    print("Döntetlen")
elif gepmutat == 0 and usermutat == 1 or \
    gepmutat == 1 and usermutat == 2 or \
    gepmutat == 2 and usermutat == 0:
    print("User győzött!")
else:
    print("Döntetlen!")
"""
