feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1007:
Kérjen be egy karaktert, majd írassa ki egymás mellé 70-szer.
"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

karakter = input("Adj meg egy karaktert: ")

for i in range(70):
	print(karakter, end="")
