feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1009:
Írjon programot, amely bekér két karaktert. Ha a karakterek egyeznek akár kisbetűs akár nagybetűs formában, akkor írja ki, hogy „Egyezik”.
Ellenkező esetben „Nem jó”."""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

kar1 = input("Adj meg egy karaktert: ")
kar2 = input("Adj meg egy másik karaktert: ")

if str.lower(kar1) == str.lower(kar2):
	print("\nEgyezik")
else:
	print("\nNem jó")
