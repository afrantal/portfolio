feladat="""Frantal Attila, 2020.11.05. , esti Szoft
Fealadat 1307:
Írjon programot, amely bekéri tanulók pontszámait egy tömbbe.
A bekérés után számítsa ki a pontok átlagát, a legnagyobb és a legkisebb számot.
Írassuk ki a kapott értékeket. A program azt is írja ki, mit kér be és mit ír ki!
------------------------------------------------------------------------------------------------
"""
print(feladat)

pontszamok = []  #ebbe a listába kérem be a pontszámokat

#pontszámok bekérése -1 végjelig
i = True
sorsz = 1 #ennyiszer fut a ciklus, kezdő értéke 1
while i:
	pont = float(input("Add meg az "+str(sorsz)+". tanuló pontszámát (-1-re vége a bekérésnek): "))
	if pont == -1:
		i = False
	else:
		pontszamok.append(pont)
		sorsz += 1

kisebb = pontszamok[0] #ebben tárolom a legkisebb elemet, kezdő értéke az első pontszám
nagyobb = pontszamok[0] #ebben tárolom a legnagyobb elemet, kezdő értéke az első pontszám
osszeg = 0.0 #ebben gyűjtöm a pontszámok összegét

for i in range(len(pontszamok)):
	if kisebb >= pontszamok[i] :
		kisebb = pontszamok[i]
	if nagyobb <= pontszamok[i]:
		nagyobb = pontszamok[i]
	osszeg += pontszamok[i]

print("\n-------------------------------eredmény-------------------------------")
print("\nAz eredeti pontszámok:", pontszamok)
print("A pontszámok átlaga:", "% .4f" % (osszeg / len(pontszamok)))
print("A legkisebb pontszám:", kisebb)
print("A legnagyobb pontszám:", nagyobb)
