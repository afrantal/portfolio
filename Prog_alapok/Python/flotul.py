#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")
"""
0205-ös feladat:
Írjon programot, amelyben egy float típusú változóban elhelyezi a 18,58 értéket, 
majd három tizedesjegy pontossággal, 17 helyen, vezető nullákkal írassa a képernyőre.
"""

print('A 18,58 értéket három tizedesjegy pontossággal, 17 helyen, vezető nullákkal írassa a képernyőre.')

a = 18.58

print('% 017.3f' % a)			#első megoldás
print('{: 017.3f}'.format(a))	#második megoldás

