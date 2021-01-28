#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")

feladat="""
0342-es feladat:
Írjon programot, amely bekéri egy szabályos ikozaéder élhosszát,
majd kiszámolja annak a köré írható gömbnek a sugarát,
amely az ikozaéder minden csúcsát érinti.
"""
print(feladat)

import math

oldal = float(input('Add meg egy szabályos ikozaéder élhosszát: '))

sugar = (oldal/4) * math.sqrt(10 + 2 * math.sqrt(5))

sugar2 = '% .4f' % sugar

print('\nAnnak a gömbnek a sugara , amely a szabályos ikozaéder köré írható \nés annak minden csúcsát érinti:', sugar2)
