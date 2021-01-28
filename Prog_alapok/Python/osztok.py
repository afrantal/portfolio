print('Adj meg egy egész számot (negatív is lehet), kiírom az osztóit.\n')

#bekérés
szam = int(input('Szám: '))

#eredmény kiíratás első része (fejléc)
print(str(szam) + ' ósztói: ', end = '')

for i in range(1,abs(szam)+1):
	if szam % i == 0:
		print(str(i) + ',', end = '')
