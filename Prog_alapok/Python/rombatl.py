#Készítette: Frantal Attila, 2020.10.01, esti Szoft
print("Készítette: Frantal Attila, 2020.10.01, esti Szoft\n")

"""
0311-es feladat:
Írjon programot, amely kiszámítja egy rombusz területét annak két átlója segítségével. Az átlók hosszát kérje be a felhasználótól.
A program első sora írja ki mit csinál a program. A program második sora az ön vezeték és keresztneve legyen, majd vessző, szóköz és az osztálya.
"""
print('Számítsa ki egy rombusz területét annak két átlója segítségével.\n')

import math

atlo1 = float(input('Add meg a rombusz egyik átlóját (cm): '))
atlo2 = float(input('Add meg a rombusz másik átlóját (cm): '))

terulet = (atlo1 * atlo2) / 2

print('A rombusz területe:', '% .2f' % terulet, 'cm2')
