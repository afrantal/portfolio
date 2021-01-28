#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")

feladat="""
0407-es feladat:
A program először saját nevét írja a képernyőre.
A neve után írassa a képernyőre mit csinál a program.
Kérjük be egy háromszög oldalait.
A program ellenőrizze, hogy a háromszög szerkeszthető-e.
Ha a háromszög nem szerkeszthető, írja ki, hogy „nem háromszög”
Ha a háromszög szerkeszthető számítsuk ki a területét, írjuk az eredményt a képernyőre.
"""
print(feladat)

import math

check = True

while check == True:  #while check:
	a = float(input("A oldal: "))
	b = float(input("B oldal: "))
	c = float(input("C oldal: "))
	if a+b>c and a+c>b and b+c>a:
		s = (a+b+c)/2
		t = math.sqrt(s*(s-a)*(s-b)*(s-c))
		k = a + b + c
		print("A háromszög területe:", end='')
		print('% .2f' % t)
		#print("A háromszög kerülete: "+str(k))
		check = False
	else:
		print("Nem háromszög, add meg újra az oldalakat!")


