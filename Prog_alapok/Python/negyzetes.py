#Frantal Attila, 2020.10.16, esti Szoft
print('Frantal Attila, 2020.10.16, esti Szoft')
"""
0254-as feladat
Vegye fel a következő változókat a következő értékekkel:
a = 15;
b = 21;
c = 13;
d = 27;
e = 33;
Számítsd ki a számok négyzetes közepét.
"""
print('\nSzámold ki a számok négyzetes közepét.\n')
print('a = 15')
print('b = 21')
print('c = 13')
print('d = 27')
print('e = 33')

import math

a = 15
b = 21
c = 13
d = 27
e = 33

negyzetes = math.sqrt((a**2 + b**2 + c**2 + d**2 + e**2)/5)

print('\nA számok négyzetes közepe:', '%.2f' % negyzetes)
