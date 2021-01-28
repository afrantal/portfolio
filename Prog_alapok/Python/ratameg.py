#Készítette: Frantal Attila, 2020.10.16, esti Szoft
print('Készítette: Frantal Attila, 2020.10.16, esti Szoft')
"""
0323-es feladat
Szeretnénk n évre betenni x összeget, amely után n év múlva kapunk y összeget. 
Nem tudjuk megéri-e. Számítsuk ki a belső megtérülési rátáját (IRR - Inter Rate of Return).

Ezt gyakran használjuk arra, hogy megnézzük gazdaságos-e pénzünket befektetni. 
Ha a befektetéshez kötődő kamatláb (például a banki kamatláb) kisebb mint a megtérülési ráta, akkor gazdaságos befektetni.

Írjon programot, amely bekéri a hány évre szeretnénk betenni a tőkénket, mennyi tőkét szeretnénk betenni, mennyit kapnánk vissza. Számítsa ki a megtérülési rátát.

A megtérülési ráta kiszámításának képlete a következő:

r = root{t}{C_t/C_0} - 1
"""
print('\nBelső megtérülési ráta (IRR) kiszámítása.\n')

ev = float(input('Lekötési évek száma: '))
toke = float(input('Lekötendő tőke: '))
vissza = float(input('Lejáratkor visszajáró összeg: '))

irr = (vissza/toke)**(1/ev) - 1

print('\nA megtérülési ráta (IRR):', '%.2f' % (irr*100), '%')
