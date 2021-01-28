"""
Írjon programot, amely bekéri a számokat 0 végjelig, miközben összegezi azokat, ha azok nagyobbak mint 49. 
Ha szám 49 vagy kisebb, akkor írjon hibaüzenet a felhasználónak.
Az összeget írassa ki az “Eredmény” szó után.
A program első sora a saját nevét és vesszővel tagolva az aktuális évszámot írja a képernyőre.
"""
print("Frantal Attila, 2020.10.01 \n")

szam = None
eredmeny = 0

while szam != 0:
	szam = int(input("Szam: "))
	if szam <= 49 and szam != 0:
		print("Hiba: 50-nél kisebb számot adtál meg. Csak 50 és annál nagyobb számokat lehet megadni.")
	else:
		eredmeny += szam

print("Eredmény: ", eredmeny)
