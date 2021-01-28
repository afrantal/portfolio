#Készítette: Frantal Attila, 2020.10.01, esti Szoft
print("Készítette: Frantal Attila, 2020.10.01, esti Szoft\n")

"""
0308-as feladat:
Számítsuk ki egy háromszög területét, a háromszög három oldalából! Kérjük be a háromszög oldalait!
"""
print('Számítsuk ki egy háromszög területét, a háromszög három oldalából! Kérjük be a háromszög oldalait!\n')

import math

i = True

while i:
	a = float(input('a = '))
	b = float(input('b = '))
	c = float(input('c = '))
	if a < b + c and b < a + c and  c < a + b :
		s = (a+b+c)/2
		print("\nA háromszög területe:", '% .4f' % (math.sqrt(s*(s-a)*(s-b)*(s-c))))
		i = False
	else:
		print("\nNem szerkeszthető a háromszög, adj meg új adatokat!\n")
