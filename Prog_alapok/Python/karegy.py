feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1053:
Írjon programot, amely bekér egy karaktersorozatot. A program írjon ki minden karaktert egyenként, de egymás alá!"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

karsor = input("Adj meg egy karakter sorozatot: ")

print() #üres sor

for i in range(len(karsor)):
	print(karsor[i])

