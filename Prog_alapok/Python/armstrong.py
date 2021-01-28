#Frantal Attila, 2020.10.01, esti Szoft
print("Frantal Attila, 2020.10.01, esti Szoft\n")
"""
Kérjen be egy n számot, majd írassa ki n darab armstrong számot.
Armstrong-számról beszélünk, ha egy n jegyű szám, minden számjegyét az n-edik hatványra emeljük és összeadjuk,
az eredeti számot kapjuk.
"""

n = int(input('Adj meg egy pozitív egész számot: '))

i = 1
szam = 0
osszeg = 0

print('Az első '+str(n)+' db Armstrong szám: ', end='')

while i <= n:									# n db számot kell visszaadnia, de előre nem tudom, hogy ehhez hányszor kell lefutnia
	for j in range(0,len(str(szam))):					#annyiszor fut le, ahány jegyű a szám
		osszeg += int(str(szam)[j])**len(str(szam))	#a K jegyű szám minden számjegyét a K-dik hatványra emelem és összeadom
	if szam == osszeg and i < n:					#ha Armstrong szám és még nincs meg az "n" db belőlük, akkor vesszővel elválasztva íratom ki
		print(str(szam)+', ',end='')
		i += 1
	elif szam == osszeg and i == n: 				#ha Armstrong szám és megvan az "n"-dik utolsó db is belőlük, akkor vessző nélkül íratom ki a végére
		print(szam,end='')
		i += 1
	szam += 1								#a számot 0-tól indítottam, ezért eggyel növelnem kell az értékét a következő futás előtt
	osszeg = 0								#az összeget nullázom, hisz ebbe kerül a következő szám számjegy-hatványainak összege
