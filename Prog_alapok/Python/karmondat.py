feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1061:
Írjon programot, amely bekér több mondatot egy karaktersorozatba. A program tömörítse a karaktersorozatot! A tömörítés a következőket jelenti:

a mondat elejéről elhagyjuk a felesleges szóközöket
a szavak között csak egy szóközt hagyunk
a pont előtt felesleges szóközöket elhagyjuk

     Első             mondat      .     Második               mondat       .       """
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

text1 = input("Adj meg több mondatot: ")
text1 = text1.strip()

for i in range(len(text1), 2, -1):
	text1 = text1.replace(' '*i,' ')

text1 = text1.replace(' .','.')

print(text1)

