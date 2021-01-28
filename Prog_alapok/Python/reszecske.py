#Készítette: Frantal Attila, 2020.10.10, esti Szoft
print("Készítette: Frantal Attila, 2020.10.10, esti Szoft\n")

"""
0302-es feladat:
Az anyagmennyiség jele az n. Mértékegysége a mol.
1 mol = 6*10^23 db részecske együttese
Kérje be hány mol konyhasója van, és írja ki fixpontos számábrázolással a részecskék számát.
"""
print('1 mol = 6*10^23 db részecske együttese.\nKérje be hány mol konyhasója van, és írja ki fixpontos számábrázolással a részecskék számát.\n')

mol = float(input('Hány mol konyhasója van: '))

darab = mol * 6 * 10**23

print("\nA részecskék száma:", '% .2f' % darab , 'db')
