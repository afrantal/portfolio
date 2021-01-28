feladat="""Frantal Attila, 2020.11.05. , esti Szoft
Fealadat 1303:
Írjon programot, amely egy valós számokat tárolni képes tömböt deklarál 7 kezdőértékkel. 
Készítsen ciklust, amely megnézi melyik a tömb legkisebb eleme, majd azt a képernyőre írja.
"""
print(feladat)

lista = [7.2,12.75,21.4,3.5,9.3,11.82,22.142]

kisebb = lista[0]  #a tömb első eleme

#végigmegyek a tömb elemein egyesével, amelyik kisebb lesz, mint a változó azt teszem a változóba
for i in range(len(lista)):
	if kisebb >= lista[i] :
		kisebb = lista[i]
print("-------------------eredmény---------------------------")
print("\nAz eredeti tömb:", lista)
print("A tömb legkisebb eleme:", kisebb)
