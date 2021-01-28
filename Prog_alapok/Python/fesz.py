print("Frantal Attila, 2020.10.01\n")

import math

input_type = int(input('Melyik 2 adatot adod meg? 1: teljesítmény, ellenállás 2: teljesítmény, áram \n'))

if input_type == 1 :
	p = float(input('teljesítmény = '))
	r = float(input('ellenállás = '))
	print("feszültség = ", math.sqrt(p*r))
else:
	p = float(input('teljesítmény = '))
	i = float(input('áram = '))
	print("feszültség = ", p/i)
