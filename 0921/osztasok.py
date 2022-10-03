print('Osztások')
print("Osztások")
print('''Osztások''')
print("""Osztások""")

print('''
Tördelt
szöveg
''')

elso = 5
masodik = 3

print(elso / masodik)   # osztás
print(elso // masodik)  # egész osztás  math.floor(elso / masodik)
print(elso % masodik)   # maradékos osztás

print(round(elso / masodik, 2)) # round metódus
print("{:.3f}".format(elso / masodik))  # format
print("%.2f"%(elso / masodik))  # jávás format