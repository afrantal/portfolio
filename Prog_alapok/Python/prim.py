#Frantal Attila, 2020.10.31., esti Szoft
feladat="""Frantal Attila, 2020.10.31., esti Szoft\n
Feladat 0734:
Írjunk ki két adott szám közötti prímszámokat.
"""
print(feladat)

#bekérés
szam1 = int(input('szám1 = '))
szam2 = int(input('szám2 = '))

#kiíratás első része (eredmény fejléc)
print('\nPrímszámok ' + str(szam1) + ' és ' + str(szam2) + ' között: ', end='')

#ebben a változóban tárolom el egy szám osztóinak darabszámát
oszto = 0
eredmeny = ''

#külső ciklusban megyek végig a számtartomány elemein
for i in range(szam1,szam2+1):
	for n in range(1 , i+1):  #belső ciklus: a külső ciklusban kiválasztott szám osztóit számolom meg
		if i % n == 0:
			oszto += 1
	if oszto == 2:            #vissza a külső ciklusba: ha pont 2 db osztója van (1 és önmaga), akkor prímszám és kiíratom
		#print(str(i) + ',',end = '')
		eredmeny += str(i) + ','
	oszto = 0                 #nullázom az osztók darabszámát a következő szám bekérése előtt

print(eredmeny+'\b ')  #leszedem az utolsó vesszőt a végéről
