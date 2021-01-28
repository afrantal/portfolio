#Frantal Attila, 2020.10.16, esti Szoft
print('Frantal Attila, 2020.10.16, esti Szoft')
"""
0313-es feladat
Írjon programot, amely kamatos kamatot számít. A feladat kiíratni a tényleges kamatot 1 évre. Bekéri a betétet a „betet” nevű változóba.
Bekéri a betét évenkénti tőkésítésének számát, amit a tokesites_szam változóban tárolunk.
Bekéri a névleges kamatot százalékban, amit a nevleges váltózóban tárolunk.

Tenyleges = ((1 + nevleges / {100 ~tokesitesekSzama}) ^ {tokesitesekSzama  }-1) *betet
"""
print('\nKamat számítás\n')

betet = float(input('Betét: '))
nevleges = float(input('Névleges kamat (%): '))
tokesites = float(input('Évenkénti tőkésítésének száma: '))

tenyleges = (1 + nevleges/(100*tokesites))**tokesites - 1

#print('A tényleges kamat %-ban:', '%.2f' % (tenyleges*100), '%')
print('\nTényleges éves kamat:', '%.2f' % (betet * tenyleges), 'Ft')
