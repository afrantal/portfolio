#Készítette: Frantal Attila, 2020.10.01, esti Szoft
print("Készítette: Frantal Attila, 2020.10.01, esti Szoft\n")

"""
0310-es feladat:
Készítsen programot, amely bekér egy rombusz oldalának hosszát és az alfa szögét. Számítsa ki a rombusz kerületét és területét.
"""
print('Kérje be egy rombusz oldalának hosszát és az alfa szögét. Számítsa ki a rombusz kerületét és területét.\n')

import math

oldal = float(input('Add meg a rombusz oldalát (cm): '))
szog1 = float(input('Add meg a rombusz egyik szögét (fok): '))

szog2 = 180 - szog1  #másik szög kiszámítása, együtt 180 fokot adnak ki

#a szog1 változóba teszem a kisebb értéket, azaz ha szog1 > szog2, akkor megcserélem őket
if szog1 > szog2:
	szog3 = szog1
	szog1 = szog2
	szog2 = szog3

magassag = oldal * math.sin(szog1*math.pi/180) #az oldalból és a kisebb szögből kiszámolom a magasságot
kerulet = oldal * 4
terulet = oldal * magassag

print('A rombusz kerülete:', '% .2f' % kerulet, 'cm')
print('A rombusz területe:', '% .2f' % terulet, 'cm2')
