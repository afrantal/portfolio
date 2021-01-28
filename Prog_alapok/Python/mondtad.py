#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1320
Egy program szavakat vagy mondatokat vár a billentyűzetről. 
Írjon programot, amely a bekért szavakat eltárolja egy tömbben. 
A szavakat vége végjelig lehessen beírni. A begépelt szavakat a program vizsgálja meg, hogy tárolva van-e. 
Ha igen, írja a képernyőre: „Ezt már mondtad”
---------------------------------------------------------------------------------
"""
print(feladat)

print('\nAdatbekérés, ha nem adsz meg szót, vége a bekérésnek.\n')

szavak = []
i = True
while i:
	szo = input('Adj meg egy szót: ')
	if szo == '':
		i = False
	elif szavak.count(szo) > 0:
		print('Ezt már mondtad')
	else:
		szavak.append(szo)
		print('Elmentettem')

print('\nElmentett szavak',szavak)
