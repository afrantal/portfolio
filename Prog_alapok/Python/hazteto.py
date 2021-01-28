#Készítette: Frantal Attila, 2020.10.10, esti Szoft
print("Készítette: Frantal Attila, 2020.10.10, esti Szoft\n")

"""
0274-es feladat:
Számolja ki, hány négyzetméter cserépre van szükség, ha adott a egy ház következő három adata:

a = 17 méter
b = 3 méter
c = 170 méter
"""
print('Számolja ki, hány négyzetméter cserépre van szükség, ha adott a egy ház következő három adata:\na tető tűzfal oldali alapja = 17 méter, magassága = 3 méter, hosszúsága = 170 méter\n')

szelesseg = 17     #a tető tűzfal oldali alapja méterben
magassag = 3       #a tető magassága méterben
hosszusag = 170    #a tető egyik oldalának hossza méterben

import math

teto_szel = math.sqrt( (szelesseg/2)**2 + magassag**2 )  #a tető másik oldalának hossza méterben
terulet = hosszusag * teto_szel * 2                      #a befedendő tető területe négyzetméterben

print("A tető területe:", '% .2f' % terulet , 'négyzetméter')
print('A tető területe egész négyzetméterre felkerekítve:' , math.ceil(terulet))
