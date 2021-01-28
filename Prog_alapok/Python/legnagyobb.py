#Frantal Attila, 2020.10.15. , esti Szoft

print('Frantal Attila, 2020.10.15. , esti Szoft\n')

"""
Adott három valós szám. Határozzuk meg közölük a legynagyobbat! A három számot ne kérjükbe, egyszerűen adjuk meg.
"""
print('A feladat 0411 megoldása.')

valos1 = 12
valos2 = 24
valos3 = 3

#ez az "if"-es megoldás
if valos2 < valos1 and valos3 > valos1:
	print(valos1)
elif valos1 < valos2 and valos3 < valos2:
	print(valos2)
elif valos1 < valos3 and valos2 < valos3:
	print(valos3)
else:
	print('Egyik sem teljesült.')

print(max(valos1,valos2,valos3))  #ez is egy jó megoldás beépített függvénnyel
