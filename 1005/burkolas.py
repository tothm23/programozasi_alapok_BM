import math

szelesseg = float(input("A fal szélessége (m): "))
magassag = float(input("A fal magassága (m): "))

terulet = szelesseg * magassag
csempe = 0.2 * 0.2

darab = terulet // csempe * 1.1
print(f"{terulet} m\u00b2 területű falhoz {math.ceil(darab)} db csempe kell")