import random

gep_dobas = random.randint(1, 6)
sajat_dobas = int(input("Dobj a dobókockával! (1 - 6) "))

gep_allas = 0
sajat_allas = 0

while True:
    sajat_dobas = int(input("Dobj a dobókockával! (1 - 6) "))

"""
if gep_dobas > sajat_dobas:
    print(f"A gép nyert! (gép: {gep_dobas} saját: {sajat_dobas})")
elif gep_dobas < sajat_dobas:
    print(f"Te nyertél! (gép: {gep_dobas} saját: {sajat_dobas})")
else:
    print(f"Döntetlen! (gép: {gep_dobas} saját: {sajat_dobas})")
"""
