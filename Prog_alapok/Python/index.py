#Frantal Attila, 2020.10.31. , esti Szoft
feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 0738:
Önnek ki kell számolnia, hogy az adott félévben mennyiségileg és minőségileg hogyan teljesített az iskolában, az elvárt szinthez képest.
Ehhez szüksége van az elért kreditpontokra és az osztályzatok átlagára.

Egy félévben az elvárt kredit nagyság: 30. Ennél persze többet is teljesíthet. Ha több tantárgy van, akkor könnyen 6.0 fölé is mehet.
A sok tantárgy elvégzése azonban jó eredménnyel persze fizikailag képtelenség.

Az elért kreditpontok és az osztályzatok átlagának szorzata, elosztva az elvárt kreditpontokkal megadja az ösztöndíjindext.

Ösztöndíjindex képlete ezek után:
osztondijindex={elertkreditpont*osztalyzat}/30

Kérje be tantárgyankénti elért kreditpontokat, a hozzájuk tartozó osztályzatot tetszőleges végjelig, majd számolja ki az adott félév ösztöndíjindexét.
Ha egy osztályzat elégtelen, a program fogadja ugyan el, de ne vegye figyelembe az ösztöndíjindex számításánál.
"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

print("A következőkben egy-egy tantárgy credit pontjait és osztályzatát add meg. 0 creditre megszakítom a bekérést.\n")

ossz_credit = 0
ossz_jegy = 0
jegy_db = 0

while True:
	credit = int(input("Credit: "))
	if credit == 0:
		break
	osztalyzat = int(input("Osztályzat: "))
	if osztalyzat == 1:
		continue
	else:
		ossz_credit += credit
		ossz_jegy += osztalyzat
		jegy_db += 1

if jegy_db == 0:
	print("\nMinden tárgyból buktál!")
else:
	osztondijindex = (ossz_credit * (ossz_jegy/jegy_db)) / 30
	print("\nÖsztöndíjindex:", osztondijindex)

