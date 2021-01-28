print("Készítette: Frantal Attila , 2020.09.24")
print("Ha a szam1 nagyobb, mint a szam2, akkor megcseréli a két számot, majd kiírja az eredeti és az új változókat,\negyébként kiírja az eredeti változókat és, hogy \"Nincs szükség cserére.\"\n")

szam1 = int(input("szam1: "))
szam2 = int(input("szam2: "))

print("Eredeti változók: szam1 =", szam1, "szam2 =", szam2)

if(szam1 > szam2):
	szam3 = szam1   #eltárolom egy ideiglenes változóban a szam1 értékét
	szam1 = szam2   #szam1 értékét szam2-re cserélem
	szam2 = szam3   #szam2 értékét az eredeti szam1 értékére cserélem, amit az ideiglenes szam3 változóban tároltam el
	print("     Új változók: szam1 =", szam1, "szam2 =", szam2)
else:
	print("Nincs szükség cserére.")

