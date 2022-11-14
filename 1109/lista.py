Lmagas = []

# feltöltés
for i in range(5):
    cm = int(input(f"{i + 1}. magasság (cm): "))
    Lmagas.append(cm)

# Egy másolat
Lmagas_eredeti = Lmagas.copy()

# Rendezés
print(f"\nRendezés nélkül: {Lmagas}")
Lmagas.sort()
print(f"Rendezéssel: {Lmagas}")

# A legmagasabb
print(f"\nLegmagasabb: {max(Lmagas)}")
print(f"A(z) {Lmagas_eredeti.index(max(Lmagas)) + 1}. ember a legmagasabb")

# Törlés
del Lmagas_eredeti[-1]
print(f"\nTörlés után: {Lmagas_eredeti}")
