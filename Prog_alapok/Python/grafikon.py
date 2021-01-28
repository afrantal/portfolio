#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1318
Adott egy tömb, amely a következő valós számokat tartalmazza:

{0.5, 0.8, 1.0, 1.2, 3.0}
Készítsen programot, amely egy grafikont készít belőle. 
A grafikon o betűket rajzol vízszintesen a képernyőre, ehhez hasonlóan:

0,50  ooooo
0,80  oooooooo
1,00  oooooooooo
1,20  oooooooooooo
3,00  oooooooooooooooooooooooooooooo

A grafikon minden sora előtt az érték is szerepeljen.
A megoldást ciklusokkal végezze el, maximum kettővel.
---------------------------------------------------------------------------------
"""
print(feladat)

tomb = [0.5, 0.8, 1.0, 1.2, 3.0]

print('Eredmény:\n')
for i in range(len(tomb)):
	print('{:.2f}'.format(tomb[i]) + '  ' +int(10*tomb[i])*'o')
