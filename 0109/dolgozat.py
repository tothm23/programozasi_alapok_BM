def atment(max_pont, elert_pont):
    valasz = False
    kovetelmeny = (float) (max_pont / 100) * 50
    eredmeny = (float) (max_pont / 100) * elert_pont

    if ((elert_pont / max_pont) * 100 >= 50):
        return True
        
    # if eredmeny >= kovetelmeny:
    #     valasz = True
    
    return valasz


max_pont = int(input("Max pont: "))
elert_pont = int(input("Elért pont: "))

if atment(max_pont, elert_pont):
    print("Átment")
else:
    print("Nem ment át")
