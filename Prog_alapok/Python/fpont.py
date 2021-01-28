#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1315
Írjon programot, amely bekéri egy dolgozat elért pontszámait, 
az eltárolt ponthatárok alapján pedig azonnal kiírja, az eredményeket.
---------------------------------------------------------------------------------
"""
print(feladat)

def jegy(p):
	if p < 60:
		return '1-es'
	elif p < 70:
		return '2-es'
	elif p < 80:
		return '3-as'
	elif p < 90:
		return '4-es'
	else:
		return '5-ös'

print('\nAdatbekérés, -1 ponra vége a bekérésnek.')
i = True
while i:
	pont = int(input('Elért pont: '))
	if pont == -1:
		i = False
	else:
		print('Érdemjegy:',jegy(pont))

