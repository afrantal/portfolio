#Frantal Attila , 2021.01.07.  Szoft I/1/E
feladat='''
Feladat:
Lennie kell benne függvénynek.
Hőmérséklet adatait kell bekérnie szombathelyi mérőállomásról.
Hozzon létre egy programot hoseg.py néven.
A program kérje be mért adatokat, majd írassa ki, hogy volt fagy. 
Fagyról 0 fok alatt beszélünk. Az adatok bekérése addig történjen, 
amíg 'vege' végjellel jelzi a felhasználó, hogy nem ad meg több adatot. 
A bemenő adatok lehetnek negatív és pozitív számok vagy nulla. 
A végjel esetén ne vizsgálja, hogy volt-e fagy.
A megoldásban szerepeljen egy függvény, amely megmondja, 
hogy adott hőmérséklet fagypont alatti vagy nem. 
A függvényt használja fel a megoldásban. 
A függvény bemenő paramétere egy hőérték, visszaadott érték pedig egy logikai érték.
'''
print('Frantal Attila , 2021.01.07.  Szoft I/1/E')
print('Ágazati 001 mintafeladat megoldása')
print(feladat)



def fagy(fok):
	if int(ho) < 0:
		return True
	else:
		return False

ho = ''
while ho != 'vége':
	ho = input('Hő: ')
	if ho != 'vége':
		if fagy(ho):
			print('Fagy volt')
		else:
			print('Nem volt fagy')
