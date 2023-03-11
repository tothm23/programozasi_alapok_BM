def névelő(szo):

    maganhangzo = "aáeéáiíoóöőuúüű"
    if szo[0] in maganhangzo or szo[0] in maganhangzo.upper():
        return "Az"
    else:
        return "A"

szo = input("Kérem a szót: ")
print(névelő(szo), szo)