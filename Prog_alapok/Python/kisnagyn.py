#Frantal Attila, 2020.10.31., esti Szoft
feladat="""
Frantal Attila, 2020.10.31., esti Szoft\n
Feladat 0710:
Írjon programot, amely bekér számokat 0 végjelig, majd kiírja a legkisebbet és a legnagyobbat.  
"""
print(feladat)

szam = None
sorsz = 1
lista = []

while szam != 0:
	szam = int(input('szam'+str(sorsz)+': '))
	if szam != 0:
		lista.append(szam)
	sorsz += 1

print("A beadott számok listája:",lista)
print("A beadott számok emelkedő sorrendben:",sorted(lista))
print("A beadott számok minimuma:",min(lista))
print("A beadott számok maximuma:",max(lista))
