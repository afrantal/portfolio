feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1005:
Kérjen be egy karaktert. Írja ki, hogy az 'n' karakter előtt vagy után van az ábécében.
"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

betu = input("Adj meg egy betűt, ami nem \'n\': ")

if str.lower(betu) < 'n':
	print("Az \'n\' betű előtt van az ábécében.")
elif str.lower(betu) > 'n':
	print("Az \'n\' betű után van az ábécében.")
