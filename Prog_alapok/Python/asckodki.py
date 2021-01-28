#Frantal Attila, 2020.10.31. , esti Szoft
feladat="""
Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 0714:
Írjon programot, amely kiírja az ASCII karaktereket és a hozzájuk tartozó kódokat. Egy sorba annyi ASCII karaktert és kódját írjon, amennyi csak elfér.
"""
print(feladat)

from string import *

for i in range(0,len(printable)):
	print(printable[i]+' '+str(ord(printable[i]))+'  ',end='')

