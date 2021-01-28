feladat='''
Az elkészítendő program bekéri három híres nő nevét, foglalkozását, illetve nemzetiségét, amely angol vagy német lehet.
Ezt a három adatot minden esetben egy-egy objektumban tárolja.
Az adatok megadását követően a program a mintának megfelelően
, a nemzetiségtől függően Ms. (angolok) vagy Frau (németek) előtaggal együtt 
kiírja az objektumokban tárolt neveket és foglalkozásokat.
a) Írjon programot hiresek.py néven!
b) Az adatok tárolására használt objektumok alapját képező osztályt a hiresek_alap.py fájl tartalmazza részben elkészítve. 
Egészítse ki az osztálydefiníciót úgy, hogy az objektumok alkalmasak legyenek a nemzetiség tárolására is!
c) Bővítse az osztályt egy olyan tagfüggvénnyel, amely a tárolt nemzetiségtől függően „Ms.” vagy „Frau” értékkel tér vissza!
d) Kérje be a felhasználótól az adatokat és tárolja őket! 
Az adatbekérést követően írja ki a megadott emberek nevének előtagját, a nevet és a foglalkozást!
'''
print(feladat)

class HíresNő:
	def __init__(self, név, foglalkozás, nemzetiség):
		self.név = név 
		self.foglalkozás = foglalkozás 
		self.nemzetiség = nemzetiség 
	def előtag(self):
		if self.nemzetiség == 'a':
			return 'Ms.' 
		else:
			return 'Frau' 

híres_nők = [] 

for _ in range(3): 
	név = input('Add meg egy híres nő nevét! ') 
	foglalkozás = input('Add meg a foglalkozását! ') 
	nemzetiség = input('Add meg a nemzetiségét (a/n)! ') 
	híres_nő = HíresNő(név, foglalkozás, nemzetiség) 
	híres_nők.append(híres_nő) 

for híres_nő in híres_nők: 
	print(híres_nő.előtag(), híres_nő.név, 'egy híres', híres_nő.foglalkozás)
