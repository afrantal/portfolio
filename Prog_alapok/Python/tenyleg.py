#Frantal Attila, 2020.10.16, esti Szoft
print('Frantal Attila, 2020.10.16, esti Szoft')
"""
0252-es feladat
Írjon programot, amely kiszámítja a tényleges kamatot, ha az évenkénti tőkésítések száma 6, a névleges kamat, 5%, 1 évről van szó, és a betett összeg 100 Ft.
Használja a következő képletet:
Tenyleges = ((1 + nevleges / {100 x tokesitesekSzama}) ^ {tokesitesekSzama - 1 }) x betet
"""
print('\nSzámold ki a tényleges kamatot, ha az évenkénti tőkésítések száma 6, a névleges kamat, 5%, 1 évről van szó, és a betett összeg 100 Ft.\n')

tokesites = 6
nevleges = 5
betet = 100

tenyleges = (1 + nevleges/(100*tokesites))**tokesites - 1

print('A tényleges kamat %-ban:', '%.2f' % (tenyleges*100), '%')
print('Tényleges éves kamat összege:', '%.2f' % (betet * tenyleges), 'Ft')
