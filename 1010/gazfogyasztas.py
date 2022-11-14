elhasznalt = int(input('Elhasznált mennyiség (m\u00B3): '))

hatosagi_fogyasztas = 100 # Hatósági fogyasztas m^3-ban
piaci_ar = 1000
hatosagi_ar = 600

print(f"Piaci ár: {piaci_ar} Ft")
print(f"Hatósági ár: {hatosagi_ar} Ft")

if elhasznalt > hatosagi_fogyasztas:
    print(f"{elhasznalt - hatosagi_fogyasztas} Ft-tal léptük túl a hatósági áras fogyasztást")
    print(f"Fizetendő összeg: {elhasznalt * piaci_ar} Ft")
else:
    print(f"Fizetendő összeg: {elhasznalt * hatosagi_ar} Ft")