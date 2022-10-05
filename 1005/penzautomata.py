penz = int(input("Mennyi pénzt szeretnél levenni?\t"))

print(f"20000 ft: {penz // 20000} db")

maradek = penz % 20000
print(f"10000 ft: {maradek // 10000} db")

maradek = maradek % 5000
print(f"5000 ft: {maradek // 5000} db")

maradek = maradek % 2000
print(f"2000 ft: {maradek // 2000} db")

maradek = maradek % 1000
print(f"1000 ft: {maradek // 1000} db")
