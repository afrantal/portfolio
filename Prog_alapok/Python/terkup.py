#Frantal Attila, 2020.10.15. , esti Szoft

print('Frantal Attila, 2020.10.15. , esti Szoft\n')

"""
Egy kör alapú kúp térfogatának kiszámolása
"""

import math

r = float(input('Add meg a kúp alapjának sugarát: '))
m = float(input('Add meg a kúp magasságát: '))

terfogat = (1/3) * (r**2) * math.pi * m

print('\nA kúp térfogata:', '% .4f' % terfogat)  #régebbi formázás

print('\nA kúp térfogata: {: .4f}'.format(terfogat))  #alternatív formázás
