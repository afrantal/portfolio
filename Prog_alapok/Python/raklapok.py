#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")
"""
0206-os feladat:
Írjon programot, ahol 5 raklap áru súlyát tároljuk. A raklapok súlya áruval együtt, kilogramban kifejezve a következő:

214,5
232,48
243,25
217,18
231,05
Tegye 5 darab változóba az egyes értékeket, majd írassa ki egy tizedesjegy pontossággal, mértékegységgel együtt.
A számok 24 helyen legyenek ábrázolva. Minden súlyérték mértékegységgel jelenjen meg egymás alatt öt sorban.
"""

print('Az 5 raklap súlya:')

a = 214.5
b = 232.48
c = 243.25 
d = 217.18
e = 231.05

print('{: 24.1f} kg'.format(a))
print('{: 24.1f} kg'.format(b))
print('{: 24.1f} kg'.format(c))
print('{: 24.1f} kg'.format(d))
print('{: 24.1f} kg'.format(e))
