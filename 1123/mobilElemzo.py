# +36 30 111 4444
# országhívó szolgáltató és a többi

# 20 - Vodafone
# 30 - Telekom
# 50 - Digi 
# 70 - Vodafone


telefonszam = input("Telefonszám: ")
szolgaltato = ""
if telefonszam[3:5] == "20":
    szolgaltato = "Vodafone"
elif telefonszam[3:5] == "30":
    szolgaltato = "Telekom"
elif telefonszam[3:5] == "50":
    szolgaltato = "Digi"
elif telefonszam[3:5] == "70":
    szolgaltato = "Vodafone"
else:
    szolgaltato = "ismeretlen"

print(f"A szolgáltatód: {szolgaltato}")