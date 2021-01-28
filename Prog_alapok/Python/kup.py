#Frantal Attila, 2020.10.16, esti Szoft
print('Frantal Attila, 2020.10.16, esti Szoft')
"""
0253-as feladat
Írjon programot, amely kiszámítja egy kúp felszínét.
A = (pi r^2) + (pi r sqrt{r^2 + h^2})
"""
print('\nSzámold ki egy kúp felszínét\n')

import math

sugar = float(input('Add meg a kúp alapjának sugarát (cm): '))
magassag = float(input('Add meg a kúp magasságát (cm): '))


felszin = math.pi * sugar**2 + math.pi * sugar * math.sqrt(sugar**2 + magassag**2)

print('\nA kúp felszíne:', '%.2f' % felszin, 'cm2')
