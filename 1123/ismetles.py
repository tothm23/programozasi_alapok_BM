nev = input("A teljes neved: ")
karakter = input("A karakter: ")
db = 0

for elem in nev:
    if karakter.lower() in elem.lower():
        db += 1

print(f"A(z) {karakter} ennyiszer szerepelt a névben: {db}")