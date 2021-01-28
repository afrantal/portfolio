feladat="""Frantal Attila, 2020.10.10, esti Szoft\n
Feladat 1054:
Írjon programot, amely bekér egy karaktersorozatot, majd kiírja fordítva!"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

karsor = input('Karaktersorozat: ')
karsor = karsor[::-1]  #megfordítom a karaktersorozatot
print() #üres sor
print(karsor)


#Ha listaként adom meg
'''
karsor = list(input('Karaktersorozat: '))
karsor = karsor[::-1]  #megfordítom a listát

print() #üres sor

#kiíratom a megfordított lista elemeit egymás után
for i in range(len(karsor)):
	print(karsor[i], end = "")
'''
