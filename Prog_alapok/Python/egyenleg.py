#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")
"""
0203-as feladat:
Írjon programot, amely tárolja az e havi bevételt és kiadást (pl: Kiadás: 280315500; Bevétel: 125270000).
Írassa ki az egyenleget, 30 szélesen, 3 tizedesjegy pontossággal, „Ft” egységként.
"""

print('Írassa ki az egyenleget, 30 szélesen, 3 tizedesjegy pontossággal, „Ft” egységként.\n')

kiadas = 280315500
bevetel = 125270000

print('Bemeneti adatok:')
print('Kiadás:', kiadas)
print('Bevétel:', bevetel)
print('\nKiíratás:')
print('{: >30.3f} Ft'.format(bevetel-kiadas))

