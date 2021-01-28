feladat="""Frantal Attila, 2020.10.10, esti Szoft\n
Feladat 1055:
Írjon egy programot, amely megszámolja, hogy egy karakterláncban hány „b” betű van!"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

karsor = input("Adj meg egy karakter sorozatot: ")
b_db = 0

for i in range(len(karsor)):
	if str.lower(karsor[i]) == 'b':
		b_db += 1

print("\n" + str(b_db) , "db \"b\" betű van a karakterláncban.")
