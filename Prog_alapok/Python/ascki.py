#Frantal Attila, 2020.10.31. , esti Szoft
feladat="""
Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 0713:
Írjon programot, amely kiírja az ASCII karaktereket a képernyőre. Az egyes jeleket egymás mellé írja a képernyőre, egy sorba amennyi kifér.
"""
print(feladat)

from string import *

#ciklus nélkül
print(printable)

#ciklussal, space-szel elválasztva
for i in range(0,len(printable)):
	print(printable[i]+' ',end='')

