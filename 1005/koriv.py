import math

a = float(input("Kérem a kör központi szögét: "))
r = float(input("Kérem a kör sugarát: "))

i = (r * math.pi / 180) * a
t = (r * r * math.pi / 360) * a

print(f"A körív hossza: {i}")
print(f"A körcikk terulete: {t}")