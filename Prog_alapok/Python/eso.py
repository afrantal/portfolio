#Frantal Attila , 2021.01.07.  Szoft I/1/E
feladat='''
Feladat:
Kérje be az aktuális hét és az előző hét csapadékmennyiségét. 
A program írja ki, hogy nőtt, csökkent vagy nem változott a csapadék mennyisége. 
A programot eso.py néven mentse.
'''
print('Frantal Attila , 2021.01.07.  Szoft I/1/E')
print('Ágazati 001 mintafeladat megoldása')
print(feladat)

print('Csapadék mennyiség milliméterben.')
aktualis = int(input('Aktuális heti csapadék: '))
elozo = int(input('Előző heti csapadék: '))

if aktualis > elozo:
	print('Több csapadék')
elif aktualis < elozo:
	print('Kevesebb csapadék')
else:
	print('Ugyanannyi csapadék')
