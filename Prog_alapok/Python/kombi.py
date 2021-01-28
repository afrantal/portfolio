#Készítette: Frantal Attila, 2020.10.16, esti Szoft
print('Készítette: Frantal Attila, 2020.10.16, esti Szoft')
'''
0327-es feladat
Írjon programot, amely egy halmaz elemeiből vett, adott nagyságú elemszámmal meghatározza hány kombináció lehetséges, ha nem lehet ismétlődés.
A számítás képlete a következő:
{n!} / { k!* (n-k)! }
A feladat, hogy kérje a halmaz elemeinek számát, a kiválasztott elemek számát, majd írja a képernyőre hány kombináció lehetséges.
'''
print('\nEgy halmaz elemeiből vett, adott nagyságú elemszámmal meghatározza hány kombináció lehetséges, ha nem lehet ismétlődés.\n')

import math

halmaz = int(input('A halmaz elemszáma: '))
valaszt = float(input('A kiválasztott elemek száma: '))

kombinacio = math.factorial(halmaz) / (math.factorial(valaszt)*math.factorial(halmaz-valaszt))

print('\nEnnyi kombináció lehetséges:', int(kombinacio) , 'db')
