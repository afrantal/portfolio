print("Frantal Attila, 2020.10.01\n")

n = int(input("Kiszámolom N db szám összegét. Add meg N-t: "))
szam = 0
osszeg = 0

for i in range(1,n+1):
	szam = int(input("szam"+str(i)+"= "))
	osszeg += szam

print(str(n)+" db szám összege: ", osszeg)


