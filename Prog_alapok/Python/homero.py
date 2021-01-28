#Frantal Attila, 2020.10.22, esti Szoft
print("Frantal Attila, 2020.10.22, esti Szoft\n")
"""
0208-as feladat:
Adott 7 hőmérséklet adat hétfőtől vasárnapig °C-ban megadva:

5,850
3,953
3,833
2,234
3,012
1,051
3,334
Az első érték hétfő, a második kedd, stb.

Vegye fel a 7 adatot 7 darab változóba, majd írassa ki a hőmérsékletet azokat egymás alá a következő módon:

1 tizedesjegy pontosság
12 helyen
a hőmérséklet érték után mértékegység szerepeljen
minden érték előtt szerepeljen melyik naphoz tartozik
a nap neve előtt és után egy „|” karakter szerepeljen.
a mértékegység után egy „|” karakter szerepeljen
minden „|” karakter előtt és után, egy darab szóköz legyen
az érték és a mértékegység között legyen egy darab szóköz
"""

print('Adott 7 hőmérséklet adat hétfőtől vasárnapig °C-ban megadva:\n')

print('5,850')
print('3,953')
print('3,833')
print('2,234')
print('3,012')
print('1,051')
print('3,334')
print('Az első érték hétfő, a második kedd, stb.\n')

print('Vegye fel a 7 adatot 7 darab változóba, majd írassa ki a hőmérsékletet azokat egymás alá a következő módon:\n')

print('1 tizedesjegy pontosság')
print('12 helyen')
print('a hőmérséklet érték után mértékegység szerepeljen')
print('minden érték előtt szerepeljen melyik naphoz tartozik')
print('a nap neve előtt és után egy „|” karakter szerepeljen.')
print('a mértékegység után egy „|” karakter szerepeljen')
print('minden „|” karakter előtt és után, egy darab szóköz legyen')
print('az érték és a mértékegység között legyen egy darab szóköz\n')

a = 5.850
b = 3.953
c = 3.833
d = 2.234
e = 3.012
f = 1.051
g = 3.334

print(' | Hétfő | {: 12.1f} °C | '.format(a))
print(' | Kedd | {: 12.1f} °C | '.format(b))
print(' | Szerda | {: 12.1f} °C | '.format(c))
print(' | Csütörtök | {: 12.1f} °C | '.format(d))
print(' | Péntek | {: 12.1f} °C | '.format(e))
print(' | Szombat | {: 12.1f} °C | '.format(f ))
print(' | Vasárnap | {: 12.1f} °C | '.format(g))
