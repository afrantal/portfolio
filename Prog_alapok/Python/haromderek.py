print("Frantal Attila, 2020.10.01\n")

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a < b + c and b < a + c and  c < a + b and a**2 + b**2 == c**2:
	print("A háromszög szerkeszthető és derékszögű.")
elif a < b + c and b < a + c and  c < a + b:
	print("A háromszög szerkeszthető, de nem derékszögű.")
else:
	print("Nem háromszög")
