#Frantal Attila, 2020.10.16, esti Szoft
print('Frantal Attila, 2020.10.16, esti Szoft')
"""
0258-as feladat
A következő kifejezés értékét írassa a képernyőre:
({sqrt{5^3*2} * sqrt{2^4}} / {2^4})^3
A programot alakítsa úgy, hogy 4 tizedesjegy pontossággal írja ki a számot, 20 szélesen.
"""
print('\nA következő kifejezés értékét írassa a képernyőre: ({sqrt{5^3*2} * sqrt{2^4}} / {2^4})^3\n','\bA programot alakítsa úgy, hogy 4 tizedesjegy pontossággal írja ki a számot, 20 szélesen.\n')

import math

kifejezes = ((math.sqrt(5**3*2) * math.sqrt(2^4)) / 2**4)**3

print('\nA kifejezés értéke:\n', '%20.4f' % kifejezes)

