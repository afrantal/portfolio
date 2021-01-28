#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")
"""
0209-es feladat:
A következőkben statisztikai adatokat dolgozunk fel a az élve születésekről Magyarországon, január hónapban.

2012 7,65 ezer fő
2013 7,49 ezer fő
2014 7,59 ezer fő
2015 8,02 ezer fő
2016 7,72 ezer fő
Tegye a születések számát 5 különböző változóba. Az évszámokat nem kötelező változóba tenni. Írassa ki az adatokat ilyen formában:

| 2012 |  7650 fő |
| 2013 |  7490 fő |
A megoldáshoz használjon formázott kimenetet.
"""

print('Feladat leírása:')
print('A következőkben statisztikai adatokat dolgozunk fel a az élve születésekről Magyarországon, január hónapban.\n')

print('2012 7,65 ezer fő')
print('2013 7,49 ezer fő')
print('2014 7,59 ezer fő')
print('2015 8,02 ezer fő')
print('2016 7,72 ezer fő')
print('Tegye a születések számát 5 különböző változóba. Az évszámokat nem kötelező változóba tenni. Írassa ki az adatokat ilyen formában:\n')

print('| 2012 |  7650 fő |')
print('| 2013 |  7490 fő |')
print('A megoldáshoz használjon formázott kimenetet.\n')

a = 7.65
b = 7.49
c = 7.59 
d = 8.02
e = 7.72
print('-------------------------------------------------')
print('Eredmény kiíratása:\n')
print('| 2012 | {: 4.0f} fő | '.format(a*1000))
print('| 2013 | {: 4.0f} fő | '.format(b*1000))
print('| 2014 | {: 4.0f} fő | '.format(c*1000))
print('| 2015 | {: 4.0f} fő | '.format(d*1000))
print('| 2016 | {: 4.0f} fő | '.format(e*1000))
