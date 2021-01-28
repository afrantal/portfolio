#Készítette: Frantal Attila, 2020.10.10, esti Szoft
print("Készítette: Frantal Attila, 2020.10.10, esti Szoft\n")

"""
0304-es feladat:
Írjon egy programot, ami kiszámítja egy hónapban egy autóval mennyibe kerül 1km megtétele.
A program a végrehajtása során kérje be az állandó költségeket (adó, garázs, stb.), a javítási költségeket, a benzinköltségeket és a megtett km-ek számát.
"""
print('Számítsa ki, hogy egy hónapban egy autóval mennyibe kerül 1km megtétele.\n')

ado = int(input('Adó (Ft): '))
garazs = int(input('Garázs (Ft): '))
javitas = int(input('Javítás (Ft): '))
benzin = int(input('Benzin (Ft): '))
km = float(input('Megtett kilóméterekszáma (KM): '))

kmktg = (ado + garazs + javitas + benzin) / km

print("\nAz autó km költsége havonta:", '% .2f' % kmktg , 'Ft')
