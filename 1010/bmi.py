tomeg = int(input("Tömeg (kg): "))
magassag = int(input("Magasság (cm): "))

bmi = tomeg / ((magassag / 100) * (magassag / 100))

print(bmi)
if bmi < 18:
    print("sovány testalkat")
elif 18 <= bmi <= 25:
    print("normál testalkat")
else:
    print("túlsúlyosság")