#Frantal Attila, 2020.12.10, Szoft 1/I/E
print("Frantal Attila, 2020.12.10, Szoft 1/I/E")
feladat='''#1601-es feladat
Írjon programot, amely bekér számokat 0 végjelig 
és kiírja egy adat.txt állományba.
'''
print(feladat)

def beker():
	szam = -1
	szamok = []
	while szam != 0:
		szam = int(input("szám: "))
		if szam != 0:
			szamok.append(szam)
	return szamok

def faljbair(szamok):
	fp = open('adat.txt','w')
	for szam in szamok:
		fp.write(str(szam))
		fp.write('\n')
	fp.close()

def nagyobb_szaz(szamok):
	szamlalo = 0
	for szam in szamok:
		if szam > 100:
			szamlalo += 1
	return szamlalo

def rendez(szamok):
	szamok.sort()
	return szamok

def kiir(szamok):
	for szam in szamok:
		print(szam, end=' ')
	print()

szamok = beker()
kiir(szamok)
szamok = rendez(szamok)
kiir(szamok)

#faljbair(szamok)
#nagy_szaz = nagyobb_szaz(szamok)
#print('Száznál nagyobb:', nagy_szaz)

