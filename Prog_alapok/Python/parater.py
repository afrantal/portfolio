#Frantal Attila, 2020.10.16, esti Szoft
print('Frantal Attila, 2020.10.16, esti Szoft')
"""
0251-es feladat
Írjon programot, amely kiszámítja egy paralelogramma területét, ha adott két oldala (a és b) és az általuk közbe zárt szög (gamma).
A paralelogramma terültszámításának képlete az alábbi:
T = a x b x sin(gamma)
"""
print('\nSzámold ki egy paralelogramma területét, ha adott két oldala (a és b) és az általuk közbe zárt szög (gamma).\n')

a_oldal = 36
b_oldal = 18
gamma = 45

import math

print('A oldal = 36 cm,', 'B oldal = 18 cm,', 'gamma = 45 fok')
print('A paralelogramma területe:', '%.2f' % (a_oldal*b_oldal*math.sin(gamma)), 'cm2')
