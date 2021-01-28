"""
Írjunk programot, amely előállítja az első 10 páros számot!
"""

print("Frantal Attila, 2020.10.01\n")

szam_db = int(input('Az első hány db páros számot akarod?: '))
szam = 2

while szam <= 2*szam_db:
	print(szam)
	szam += 2
