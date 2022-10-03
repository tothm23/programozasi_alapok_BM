eke = 5
sebesseg = int(input("Traktor sebesség (km/h): "))
terulet = int(input("Felszántandó terület (ha): "))

m2 = terulet * 10000    # terület (m2)
ms = sebesseg / 3.6     # sebesség (m/s)

masodpercenkent = eke * ms  # mp-enként hány m2


ido = terulet/ ms
ora = ido // 3600
marad = ido % 3600
perc = marad // 60

eredmeny = m2 / masodpercenkent # mp-enkénti eredmény




print("Idő:")
print(f"{ora} óra, {perc} perc")