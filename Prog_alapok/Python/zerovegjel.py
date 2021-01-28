#Frantal Attila, 2020.10.31. , esti szoft
feladat="""
Frantal Attila, 2020.10.31. , esti szoft\n
Feladat 0701:
Készítsen programot amely összeadja a bekért számokat 0 végjelig!  
"""

print(feladat)

szam = None
osszeg = 0
i = 1

while szam != 0:
	szam = int(input('szám'+str(i)+': '))
	i += 1
	osszeg += szam

print("A beadott számok összege:",osszeg)
