#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1323
Adott a következő mátrix:
85	47	27	81	32
27	44	11	87	28
81	12	33	21	76
68	76	44	37	56
69	90	42	89	48
Tárolja el egy tömbben, majd írassa ki a főátlóját.
---------------------------------------------------------------------------------
"""
print(feladat)

matrix = [[85,47,27,81,32],[27,44,11,87,28],[81,12,33,21,76],[68,76,44,37,56],[69,90,42,89,48]]

print('A mátrix:')
for i in range(5):
	for j in range(5):
		print(matrix[i][j], end=' ')
	print()

print('\nA mátrix főátlója:')
for i in range(5):
	for j in range(5):
		if i == j:
			print(matrix[i][j], end=' ')
		else:
			print('  ', end=' ')
	print()
