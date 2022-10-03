"""
    Köregyenlet
    @author tothm
"""

"""
    Tesztadatok:
    P(-2,1)
    C(-3,-2)
    r = 4.9
"""

import math

def koregyenlet(u, v, x, y):
    return round(math.sqrt(math.pow(x - u, 2) + math.pow(y - v, 2)), 2)

def main():
    print("A kör középpontja \t C(u,v)")
    u = int(input("u = "))
    v = int(input("v = "))

    print("\nA kör vonala \t p(x;y)")
    x = int(input("x = "))
    y = int(input("y = "))

    print(f"\nA kör sugara: \t r = {koregyenlet(u, v, x, y)}")

if __name__ == "__main__":
    main()