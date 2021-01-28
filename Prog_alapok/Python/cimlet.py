#Frantal Attila, 2020.10.31., esti Szoft
feladat="""Frantal Attila, 2020.10.31., esti Szoft\n
Feladat 0732:
Írjon programot, amely bekéri egy kifizetendő fizetés összegét, majd kiszámolja hogyan lehet a legkevesebb címletben kifizetni.
"""
print(feladat)


szam = int(input('Kifizetendő fizetés összege = '))

#ha 1,2,3,4,6,7,8,9-re végződik a szám, akkor kerekíteni kell, mert 5 Ft-os a legkisebb érménk
if szam % 5 in (1,2):   #1,2,6,7 végződésnél lefele kerekítünk
	szam = szam - (szam % 5)
	print('Kerekített összeg = ',szam, '\n')
elif szam % 5 in (3,4):  #3,4,8,9 végződésnél felfele kerekítünk
	szam = szam - (szam % 5) + 5
	print('Kerekített összeg = ',szam, '\n')

sumdb = 0

for i in (20000,10000,5000,2000,1000,500,200,100,50,20,10,5):
	db = szam // i
	print(('%5d' % i) + ' Ft-os: ' + ('%5d' % db) + ' db')
	szam = szam % i
	sumdb += db

print('\nÖsszes címlet: ' + str(sumdb) + ' db')
