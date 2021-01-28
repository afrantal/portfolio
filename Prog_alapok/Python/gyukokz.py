print("Frantal Attila, 2020.10.01\n")

import math
szam = None

while szam != 0:
	szam = int(input("szám = "))
	if szam != 0:
		print("Négyzetgyök "+str(szam)+" = ",math.sqrt(szam))

