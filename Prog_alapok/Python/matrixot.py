#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1311
Írjon programot, amely egy 4×4-es mátrix minden elemét 5-ös számmal tölti fel.
"""
print(feladat)

matrix = [[],[],[],[]]

for i in range(4):
	for k in range(4):
		matrix[i].insert(k,5)

for i in range(4):
	for j in range(4):
		print(matrix[i][j], end=' ')
	print()
