'''
A feladatban elkészítendő program bekéri három film címét, illetve percben kifejezett hosszát. 
Egy-egy filmcím-filmhossz adatpár megadását követően a program a percben kifejezett időtartamot átszámolja órákra és pecekre – például a 61 percet 1 óra 1 percre. 
Az eredményt a film címével együtt kiírja.
A program üzeneteinek megfogalmazásában kövesse az alábbi példát! 
Azokat a részeket, amiket a felhasználó gépel be, a mintában vastagított és döntött betűkkel emeltük ki.
A program kiindulási alapja a filmalap.py fájlban található. 
Ennek felhasználásával írjon programot kedvencfilm.py néven! 
Egészítse ki a megkapott függvényt úgy, hogy az alkalmas legyen percben megadott időtartamot órában és percben visszaadni! 
A program többi részében használja az így kiegészített függvényt!
'''

def oraperc(idotartam):
	return str(idotartam//60) + ' óra ' + str(idotartam%60) + ' perc '

for i in range(3):
	film = input('Add meg egy film címét! ')
	perc = int(input('Hány perces a film? '))
	print('A(z) ' + film + ' című film ' + oraperc(perc))
