#Frantal Attila, 2020.10.31.,esti Szoft

feladat="""
Frantal Attila, 2020.10.31. ,esti Szoft
Feladat 0716:
Írjon programot, amely az alábbi szabályos fordított piramist rajzolja a képernyőre:
@ @ @ @ @ @ @ @ @
  @ @ @ @ @ @ @ 
    @ @ @ @ @
      @ @ @
        @
"""
print(feladat)
print('------eredmény------\n')
szam = 9

for i in range(0,5):
	print(" "*i*2 + "@ "*(szam-i*2))

