def sikeres(pont):
	if pont>=48:
		return True
	else:
		return False

nev = None

while nev != '':
	nev = input('Add meg a vizsgázó nevét! ')
	if nev:
		pontszam = int(input('Add meg a pontszámát! '))
		if sikeres(pontszam):
			print(nev, 'vizsgája sikeres.')
		else:
			print(nev, 'vizsgája sikertelen.')
