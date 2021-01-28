def multiple(lista):
	sum = 1
	for i in lista:
		sum *= i
	return sum

def multinumber():
	lista = []
	for i in range(0,5,1):
		num = int(input('Szám: '))
		lista.append(num)
	multiplenum = multiple(lista)
	print('A szorzat: {:^10}'.format (multiplenum))

multinumber()
