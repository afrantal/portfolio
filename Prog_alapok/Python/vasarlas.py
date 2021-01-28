print("Frantal Attila, 2020.10.01\n")


liszt = int(input('liszt = '))
mez = int(input('mez = '))
tej = int(input('tej = '))
fizetendo = liszt*300 + mez*1000 + tej*200

print("Fizetendő összeg:", fizetendo)

if fizetendo > 10000 :
	print("Nincs elég pénzed!")

