feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1056:
Írjon egy programot, amely megszámolja, hogy egy karakterláncban hány magánhangzó van!"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

karlanc = input("Adj meg egy karakterláncot: ")
m_db = 0
maganhangzok = ['a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű']

for i in range(len(karlanc)):
	if str.lower(karlanc[i]) in maganhangzok:
		m_db += 1

print("\n" + str(m_db) , "db magánhangzó van a karakterláncban")
