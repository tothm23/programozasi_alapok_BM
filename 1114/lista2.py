import random

lista = [random.randint(1, 5) for x in range(5)]
van = False
for i in range(len(lista) - 1):
    if lista[i] + 1 == lista[i + 1]:
        van = True
        break
print(lista)
print(van)