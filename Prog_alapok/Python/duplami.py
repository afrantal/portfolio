feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1008:
Írjon programot, amely megkérdezi, milyen számokkal szeretnénk dolgozni: „Egész/Valós?” A program kérjen be egy 'E' vagy egy 'V' betűt. 
Ha a felhasználó 'E' betűt választja akkor deklaráljunk egy egészeket tárolni képes változót és kérjünk be egy egész számot. 
Ha a 'V' betűt valós számokat tárolni képes változót deklaráljunk és kérjünk be egy valós számot. 
A bekért értéket szorozzuk meg kettővel, az eredményt írjuk a képernyőre."""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

tipus = input("\"E\"gész / \"V\"alós számot adsz meg? ")

if str.upper(tipus) == "E":
	egesz = int(input("Adj meg egy egész számot: "))
	print("Eredmény:", egesz*2)
elif str.upper(tipus) == "V":
	valos = float(input("Adj meg egy valós számot: "))
	print("Eredmény:", valos*2)
else:
	print("Csak E-t vagy V-t kellett volna a legelején megadnod!")
