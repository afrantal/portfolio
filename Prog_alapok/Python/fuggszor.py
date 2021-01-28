#Frantal Attila, 2020.11.12, Szoft1 esti
feladat="""Frantal Attila, 2020.11.12, Szoft1 esti\n
Feladat 1903:
Készítsen függvényt, amely bekér két számot, majd visszaadja azok szorzatát.
"""
print(feladat)

def dupla(szam1,szam2):
	return szam1 * szam2

szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy másik számot: "))

print("\nA két szám szorzata:", dupla(szam1,szam2))
