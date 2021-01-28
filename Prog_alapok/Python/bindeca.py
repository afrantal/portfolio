"""
Kérjen be egy bináris számot, majd írja ki decimálisan.      
"""

szamrend = int(input("Számrendszer: "))
szam = input("Adj meg egy számot a megadott számrendszerben: ")
hossz = len(szam)
sorsz = 0
deci = 0

for i in range(hossz-1, -1, -1):
	deci += (szamrend ** i) * int(szam[sorsz])
	sorsz += 1

print("A szám értéke a 10-es számrendszerben:",deci)

