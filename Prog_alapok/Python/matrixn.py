#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1312
Írjon programot, amely bekér egy számot, amely egy mátrix két dimenzióját határozza meg.
Ha meg vannak a dimenziók kérje be a mátrix minden elemét.
"""
print(feladat)

dimenzio = int(input('Add meg a mátrix dimezióját: '))

print()

matrix = []
for i in range(dimenzio):
	m = []
	for k in range(dimenzio):
		n = int(input('Add meg a mátrix '+str(i+1)+'. sor '+str(k+1)+'. oszlop elemét: '))
		m.append(n)
	print()
	matrix.append(m)

print('\nEredmény mátrix:\n')

for i in range(dimenzio):
	for j in range(dimenzio):
		print(matrix[i][j], end=' ')
	print()
