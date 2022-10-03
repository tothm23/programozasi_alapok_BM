import math

darab = int(input("A labdák száma: "))
d = 23

"""
    1 szalag:   (2 * d / 2 * PI)
    2 szalag:   2 * (2 * d / 2 * PI)
    masnival:   2 * (2 * d / 2 * PI) + 60
    x db labda: (2 * (2 * d / 2 * PI) + 60) * darab
    cm-ben:     (2 * (2 * d / 2 * PI) + 60) * darab
    m-ben:      (2 * (2 * d / 2 * math.pi) + 60) * darab // 100 + 1
"""

szalag = (2 * (2 * d / 2 * math.pi) + 60) * darab // 100 + 1
print(f"Szalagok m-ben : {szalag}")