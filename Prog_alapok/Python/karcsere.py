feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1059:
Írjon programot, amely bekér egy karaktersorozatot, majd bekér egy másikat amely megmondja mit is szeretnénk benne lecserélni.
Kérjün be egy harmadik karakterláncot is, amely megmondja mire szeretnénk cserélni a másodiknak bekért szöveget."""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

karsor = input("Adj meg egy karaktersorozatot: ")
mit = input("Add meg, hogy mit cseréljünk ki: ")
mire = input("Add meg, hogy mire cseréljünk ki: ")

print("\n" + karsor.replace(mit,mire))
