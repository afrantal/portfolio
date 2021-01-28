#Frantal Attila, 2020.10.01 , esti Szoft

feladat="""
Frantal Attila, 2020.10.01, esti Szoft\n
Feladat 0709:
Írjon programot, amely bekér egy számot, majd kiírja a faktoriálisát.
"""
print(feladat)

n = int(input("Add meg N-t, kiírom a faktoriálisát. N = "))
faktor = 1

for i in range(1,n+1):
	faktor *= i

print(n,"faktoriális = ", faktor)


