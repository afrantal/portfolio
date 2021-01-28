#Frantal Attila , 2021.01.07.  Szoft I/1/E
feladat='''
Feladat:
Lennie kell osztály használatnak, modulhasználatnak, fájlkezelésnek.

A következő feladatban eladó kocsik adatait tároljuk egy fájlban. 
A fájl beolvasása után, ki kell íratnia azoknak a kocsiknak az adatait, 
amelyek ár kevesebb mint 1 millió. Utána ki kell íratnia egy újabb sorban, 
azokat amik 1 millió forint alatti áron vannak és fehérek.

Írjon programot, jarmu.py néven.
A programot Objektum Orientáltan kell megoldania.
A program forráskódjában szerepeljen megjegyzésben és külön kiíratva:
neve
osztálya
készítés dátuma
A járművek számára hozzon létre egy külön osztályt Jarmu néven, külön fájlba.
Az adattárolásnál használja Jarmu osztályt.
Olvassa be a következő fájl tartalmát, tárolja el egy megfelelő adatszerkezetben.
Ügyeljen arra, hogy az első sor a mezőneveket tartalmazza.
Írjon tagfüggvényt, amely megszámolja hány fehér jármű van.
A tagfüggvény neve feher() legyen.
Az eredményt írassa a képernyőre.
Írjon tagfüggvényt olcso() néven
A tagfüggvény, írja ki azoknak a kocsiknak az adatait, amelyek ára kevesebb mint 1 millió.
Kiírva csak a rendszám, szín és márka legyen.
Írjon újabb tagfüggvényt feherOlcso() néven, amely
kiírja azoknak a kocsiknak az adatait egy feherOlcso.txt fájlba, amelyek olcsóbbak mint 1 millió és fehér színűek.
'''
print('Frantal Attila , 2021.01.07.  Szoft I/1/E')
print('Ágazati 003 mintafeladat megoldása')
print(feladat)

from jarmu import Jarmu

class Eladas:
	def beolvas(self):
		self.jarmuvek = []
		fp = open('jarmu.txt', 'r', encoding="utf-8")
		lines = fp.readlines()        
		for line in lines[1:]:
#			line = line.rstrip()            
			(az, rendszam, szin, marka, ar) = line.rstrip().split(':')
			jarmu = Jarmu(az, rendszam, szin, marka, int(ar))
			self.jarmuvek.append(jarmu)
		fp.close()

	def feher(self):
		feherek = 0
		for jarmu in self.jarmuvek:
			if jarmu.szin == 'fehér':
				feherek += 1 
		print('Fehérek:', feherek)
 
	def olcso(self):
		print('Olcsók:')
		for jarmu in self.jarmuvek:
			if jarmu.ar < 1000000:
				print(jarmu.rendszam, jarmu.szin, jarmu.ar)
 
	def feherOlcso(self):
		print('Fehér olcsók:')
		fp = open('feherOlcso.txt','w')
		for jarmu in self.jarmuvek:
			if jarmu.ar < 1000000 and jarmu.szin == 'fehér':
#				print(jarmu.rendszam, jarmu.szin, jarmu.ar)
				fp.write(jarmu.az + ';' + jarmu.rendszam + ';' + jarmu.szin + ';' + jarmu.marka + ';' + str(jarmu.ar) + '\n')
		fp.close()


eladas = Eladas()
eladas.beolvas()
eladas.feher()
eladas.olcso()
eladas.feherOlcso()
