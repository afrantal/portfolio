#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1313
írjon programot, amely 8×8-as sakktáblán eltárolja a bábuk helyzetét. 
A programból lehessen lekérdezni milyen bábu áll egy adott helyen. 
A bábuk jelzése a következők lehetnek:

B bástya
H huszár
F futó
K király
N királynő
---------------------------------------------------------------------------------"""
print(feladat)

sor = 8 #int(input('Add meg a mátrix sorainak számát: '))
oszlop = 8 #int(input('Add meg a mátrix oszlopainak számát: '))

matrix = []
for i in range(sor):
	m = []
	for j in range(oszlop):
		elem = '□' #int(input('Add meg a mátrix '+str(sor+1)+'. sor '+str(oszlop+1)+'. oszlop elemét: '))
		m.append(elem)
#	print()
	matrix.append(m)

print('\nSakk tábla a megadott bábukkal:\n')

matrix[0][2] = 'B'
matrix[1][3] = 'H'
matrix[4][7] = 'F'
matrix[7][5] = 'K'
matrix[5][3] = 'N'

for i in range(sor):
	for j in range(oszlop):
		print(matrix[i][j], end=' ')
	print()

print()
x = int(input('Add meg az X koordinátát: '))
y = int(input('Add meg az Y koordinátát: '))
print()

if matrix[y-1][x-1] == 'B':
	print('Bástya')
elif matrix[y-1][x-1] == 'H':
	print('Huszár')
elif matrix[y-1][x-1] == 'F':
	print('Futó')
elif matrix[y-1][x-1] == 'K':
	print('Király')
elif matrix[y-1][x-1] == 'N':
	print('Királynő')
else:
	print('Üres hely')
