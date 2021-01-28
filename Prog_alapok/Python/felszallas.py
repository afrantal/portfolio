print("Frantal Attila, 2020.10.01\n")


szelseb = int(input('Szélsebesség (km/h) = '))

while szelseb < 0 or szelseb > 500:
	print("A szélsebesség nem lehet negatív, és maximum 500 lehet.")
	szelseb = int(input('Szélsebesség (km/h) = '))

szelirany = int(input('Szélirány = '))

while szelirany < 0 or szelirany > 180:
	print("A szélirány 0 és 180 fok közé essen.")
	szelirany = int(input('Szélirány = '))

felho = int(input('Felhősödés = '))

while felho < 0 or felho > 100:
	print("A felhősödés 0 és 100 közé essen.")
	felho = int(input('Felhősödés = '))

if szelseb > 50 and szelirany > 30:
	print('Nem ajánlott a felszállás!')
elif szelseb > 100:
	print('Tilos a felszállás!')
elif felho > 45:
	print('Tilos a felszállás!')
else:
	print('Szabad a felszállás.')
