#Frantal Attila, 2020.10.31., esti Szoft
feladat="""Frantal Attila, 2020.10.31., esti Szoft\n
Feladat 0733:
Kérjünk be járművek típusait tetszőleges végjelig. Számoljuk meg a bevitt járműveket, készítsünk százalékos kimutatást, a különböző típusokról.
"""
print(feladat)

#feltöltöm, hogy milyen értékeket használhat a user, ő adja meg első körben
fajta = None
tipusok = []

while fajta != '0':
	fajta = input('Jármű típusok feltöltése, amik közül választhatsz (0-ra kilépsz): ')
	if fajta != '0':
		tipusok.append(fajta)

print('\nEzek közül választhatsz a feltöltéskor:', tipusok, '\n')

#megadja a jármű típusokat a fenti listából, ha olyat ad meg, amit nem vett fel előzőleg, akkor megszakad a felvétel
i = True
tipus = ''
lista = []

while i:
	tipus = input('Jármű típusa (ha nem a fenti listából adsz meg, akkor kilépsz): ')
	if tipus in tipusok:
		lista.append(tipus)
	else:
		i = False

print() #tagolás miatt üres sor legyen

print('Járművek száma:',len(lista), '\n')

for j in range(0,len(tipusok)):
	print(tipusok[j] + ' aránya:','%5.4f' % (lista.count(tipusok[j])/len(lista)))

