#Frantal Attila , 2020.11.27 . Szoft I/1/E
print('Frantal Attila , 2020.11.27 . Szoft I/1/E \n')
feladat="""Feladat 1317
Írjon programot, emberek neveit és az IQ-jukat kéri be. 
A program írja ki kinek nagyobb az IQ-ja 80-nál.
---------------------------------------------------------------------------------
"""
print(feladat)

iq_dict = {}

print('Adatbekérés, ha nem adsz meg nevet, akkor vége a bekérésnek.')
i = True
while i:
	nev = input('Add meg a nevet: ')
	if nev == '':
		i = False
	else:
		iq = int(input('Add meg az IQ-ját: '))
		iq_dict[nev] = iq

print('\nAz alábbi személyeknek nagyobb az IQ-ja 80-nál:')
for k in iq_dict.keys():
	if iq_dict.get(k) > 80:
		print(k)
