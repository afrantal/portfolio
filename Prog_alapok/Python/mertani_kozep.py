import math

def calcMiddle(list):
	multiple = 1
	for i in list:
		multiple *= i
	result = pow(multiple,1/len(list))
	return result

def middle():
	list = []
	for i in range(0,5):
		number = int(input('Szám: '))
		list.append(number)
	result = calcMiddle(list)
	print('A mértani közép: {:>20.3f}'.format(result))


middle()
