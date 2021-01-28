#Frantal Attila, 2020.10.31., esti Szoft
feladat="""Frantal Attila, 2020.10.31., esti Szoft\n
Feladat 0731:
A program első sora a saját nevét és vesszővel tagolva az aktuális évszámot (készítés ideje) írja a képernyőre.
A program második sorában ciklusutasítással, egyetlen „*” karakter kiíratásával húzzon egy vízszintes vonalat.
A csillagokból álló vonal 80 karakter széles legyen, és minden 5-dik csillag helyén egy „-” kötőjel álljon.
"""
print(feladat)

sor = ''

for i in range(1,81):
	if i % 5 != 0:
		sor += '*'
	else:
		sor += '_'

print(sor)
