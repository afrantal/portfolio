#Frantal Attila, 2020.11.12, Szoft1 esti
feladat="""Frantal Attila, 2020.11.12, Szoft1 esti\n
Feladat 1905:
Készítsen függvényt, amely paraméterül egy számot fogad, majd visszaadja a felét. A függvény neve legyen felez.
"""
print(feladat)

def felez(szam1):
	return szam1 / 2

szam1 = int(input("Adj meg egy számot: "))

print("\nA szám fele:", felez(szam1))
