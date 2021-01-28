#Frantal Attila, 2020.10.31.,esti Szoft

feladat="""
Frantal Attila, 2020.10.31. ,esti Szoft\n
Feladat 0718:
Írjon programot amely bekér egy páratlan számot. A következő sorba ennyi „@” karaktert ír ki, de minden karakter után legyen egy üres hely.
Az utána következő sorba 2-vel kevesebb „@” karaktert írjon, de két karakter hellyel beljebb írja.
Minden ezt következő sorba ugyanígy 2-vel kevesebbet írjon ki.
Az utolsó sorba csak egyetlen karakter legyen. Például 9 beírt szám esetén így néz ki a kiírt alakzat:
@ @ @ @ @ @ @ @ @
  @ @ @ @ @ @ @ 
    @ @ @ @ @
      @ @ @
        @
"""
print(feladat)

paratlan = int(input("Adj meg egy páratlan számot: "))

for i in range(0,paratlan):
	print(' '*i*2 + '@ '*(paratlan-i*2))
