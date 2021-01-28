print("Frantal Attila, 2020.10.01\n")

szam = None
osszeg = 0
oszto = 0

while szam != 0:
	szam = int(input("szám: "))
	if szam != 0:
		oszto += 1
		osszeg += szam

print("átlag: ", osszeg/oszto)


