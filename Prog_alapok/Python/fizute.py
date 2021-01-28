#Frantal Attila, 2020.10.01, esti Szoft
print("Frantal Attila, 2020.10.01, esti Szoft\n")
"""
0202-es feladat:
Írjon programot, amelyben adott egy név és egy fizetés. 
Írja ki a nevet 30 szélesen jobbra igazítva, azt következő sorban a fizetést szintén 30 szélesen Ft utótaggal.
"""

print('Írja ki a nevet 30 szélesen jobbra igazítva, azt következő sorban a fizetést szintén 30 szélesen Ft utótaggal.\n')

nev = 'Példa Piroska'
fizetes = 220000

print('Bemeneti adatok:')
print('Név:', nev)
print('Fizetés:', fizetes)
print('\nKiíratás:')
print('{: >30s}'.format(nev))
print('{: >30d} Ft'.format(fizetes))
