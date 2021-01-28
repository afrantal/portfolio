#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")
"""
0204-as feladat:
Írjon programot, amely a következő hőmérséklet adatokat, valós számok alakjában tárolja:

15,82
18,27
22,40
23,19
24,57
22,02
20,28
Az adatok hétfőtől vasárnapig egy hét adatait tartalmazzák. A program írja ki egymás alá az adatokat.

A sorok a hőmérséklet adat értéket mutassák először, 1 tizedesjegy pontossággal, 15 szélesen, jobbra igazítva, előjellel,
a következő oszlop 10 szélességben, balra igazítva mutassa milyen napra esett.
"""

print('A sorok a hőmérséklet adat értéket mutassák először, 1 tizedesjegy pontossággal, 15 szélesen, jobbra igazítva, előjellel\n,a következő oszlop 10 szélességben, balra igazítva mutassa milyen napra esett.\n')

a = 15.82
b = 18.27
c = 22.40
d = 23.19
e = 24.57
f = 22.02
g = 20.28

print('% +15.1f' % a, 'Hétfő'.ljust(10))
print('% +15.1f' % b, 'Kedd'.ljust(10))
print('% +15.1f' % c, 'Szerda'.ljust(10))
print('% +15.1f' % d, 'Csütörtök'.ljust(10))
print('% +15.1f' % e, 'Péntek'.ljust(10))
print('% +15.1f' % f, 'Szombat'.ljust(10))
print('% +15.1f' % g, 'Vasárnap'.ljust(10))
