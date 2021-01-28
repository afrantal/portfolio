#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1316
Írjon programot, amely bekéri egy dolgozat elért pontszámait és a tanulók neveit, 
az eltárolt ponthatárok alapján pedig kiírja, az eredményeket.
---------------------------------------------------------------------------------
"""
print(feladat)

pontok = {} #szótár, amiben tárolom a tanulók neveit és elért pontszámaikat

print('Adatbekérés, ha nem adsz meg nevet, akkor vége a bekérésnek.')
i = True
while i:
	nev = input('Add meg a tanuló nevét: ')
	if nev == '':
		i = False
	else:
		pont = int(input('Add meg az elért pontját: '))
		pontok[nev] = pont

print('\nA tanulók osztályzatai:')
for k in pontok.keys():
	if pontok.get(k) <= 50:
		print(k, 'érdemjegye:', 1)
	elif pontok.get(k) <= 65:
		print(k, 'érdemjegye:', 2)
	elif pontok.get(k) <= 80:
		print(k, 'érdemjegye:', 3)
	elif pontok.get(k) <= 90:
		print(k, 'érdemjegye:', 4)
	else:
		print(k, 'érdemjegye:', 5)

