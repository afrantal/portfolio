#Frantal Attila, 2020.10.31. , esti Szoft
feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 0736:
Írjon programot, amely elektromos készülékben található ellenállások értékeit kéri be valamilyen végjelig. Ügyeljen arra, hogy az ellenállás értéke 0 is lehet.
A program kérje be sorosan vagy párhuzamosan kötött ellenállásokról van-e szó, majd ennek megfelelően számítsa ki az eredő ellenállást.

Az eredő ellenállás számítása soros kapcsolás esetén:
R_S = R_1 + R_2 + ... + R_n = sum {i=1}{n} {R_i}

Az eredő ellenállás számítása soros kapcsolás esetén:
{1/R_p} = {1/R_1} + {1/R_2} + ... + {1/R_n} = sum {i=1}{n} {R_i}
másként:
{R_p} = {1/{{1/R_1} + {1/R_2} + ... + {1/R_n}}}

A program első sora a saját nevét írja a képernyőre.
"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

tipus = input("Add meg a kapcsolás típusát, \"s\" = soros, \"p\" = párhuzamos: ")

print("\nA következőkben ellenállás értékeket kérek be, -1-re kilépek a bekérésből!\n")

eredo = float(0)

while True:
	ellenallas = float(input("Adj meg egy ellenállást: "))
	if ellenallas == -1:
		break
	elif ellenallas == 0:
		continue
	elif tipus == 's':
		eredo += ellenallas
	elif tipus == 'p':
		eredo += 1/ellenallas

if tipus == 's':
	print("\nAz eredő ellenállás soros kapcsolásnál:", eredo)
else:
	print("\nAz eredő ellenállás párhuzamos kapcsolásnál:", "% .4f" % (1/eredo))

