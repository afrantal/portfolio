"""
Tamagocsi program
"""

ehezes = 0
szomjazas = 0
cmd = ''
halal = False

while cmd != 'vege':
	ehezes += 1
	szomjazas += 1
	if cmd == 'etet es itat':
		ehezes -= 4
		szomjazas -= 5
	if cmd == 'etet':
		ehezes -= 4
	if cmd == 'itat':
		szomjazas -= 5
	if ehezes > 7 and szomjazas > 9:
		print('Éhezek és szomjazok!')
	elif ehezes > 7:
		print('Éhezek!')
	elif szomjazas > 9:
		print('Szomjazok!')
	cmd = input('Tama: ')
	if ehezes > 15 or szomjazas > 15:
		halal = True
	if halal == True:
		print('Meghaltam')
		cmd = 'vege'
