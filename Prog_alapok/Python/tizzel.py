#Frantal Attila, 2020.10.31., esti Szoft
feladat="""Frantal Attila, 2020.10.31., esti Szoft\n
Feladat 0719:
A program első sora a saját nevét és vesszővel tagolva az aktuális évszámot írja a képernyőre.
Írjon programot, amely kiírja a számokat 1-től 100-ig. Egy sorba 10 számot írjon ki jól láthatóan elkülönítve.
"""
print(feladat)

sor=''

for i in range(1,101):
	if i % 10 != 0:
		sor += ('%4d' % i)+','
	else:
		sor += ('%4d' % i)+'\n'
		print(sor)
		sor = ''
