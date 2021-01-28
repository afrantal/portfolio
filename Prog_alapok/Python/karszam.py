feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1060:
Írjon programot, amely bekér egy karaktersorozatot, majd megszámolja hány szám karakter van benne!"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

karsor = input("Adj meg egy karaktersorozatot: ")
szamok = ['0','1','2','3','4','5','6','7','8','9']
szam_db = 0


for i in range(len(karsor)):
	if karsor[i] in szamok:
		szam_db += 1

print("\n" , szam_db, 'db szám van benne')
