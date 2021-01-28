'''
Az elkészítendő program főneveket kér be a felhasználótól – összesen hármat – és a főnév felhasználásával egyszerű mondatokat alkot. 
A mondatok három szóból állnak: Az „a” vagy az „az” névelőből, a főnévből és egy véletlenszerűen választott jelzőből. 
A program működését az alábbi minta szemlélteti:
a) Írjon programot „mondatok.py” néven! Rendelkezésére áll a mondatok_alap.py fájl, benne egy félig megírt függvénnyel névelő() néven. 
    E függvény feladata a főnévhez illeszkedő névelő meghatározása. Egészítse ki úgy a függvényt úgy, hogy „a” névelőt adjon vissza, 
    ha a szó magánhangzóval kezdődik, és „az” névelőt minden más esetben! Használja a függvényt a feladat további részének elkészítése során!
b) Kérjen be három főnevet a felhasználótól! Határoztassa meg a főnévhez illeszkedő névelőt a kiegészített névelő() függvénnyel!
c) A mondatok_alap.py fájlban található, előre elkészített jelző() nevű függvény a benne tárolt három jelző közül ad egyet véletlenszerűen vissza. 
Írja ki a soron következő főnév névelőjét, magát a főnevet és egy jelzőt!
A program üzeneteinek megfogalmazásában kövesse az alábbi példát! Azokat a részeket, amiket a felhasználó gépel be, 
a mintában vastagított és döntött betűkkel emeltük ki.
'''

def nevelo(szo):
	maganhangzok = 'aáeéiíoóöőuúüű' 
	if szo[0].lower() in maganhangzok:
		return 'Az'
	else:
		return 'A'

import random

def jelzo():
	melleknev = ['piros', 'nagy', 'könnyed']
	return melleknev[random.randrange(0,3,1)]

print('Adj meg három főnevet!') 
for szam in range(1,4):
	fonev = input(str(szam) + '. főnév: ') 
	print(nevelo(fonev).capitalize(), ' ', fonev, ' ', jelzo(), '.', sep='')

