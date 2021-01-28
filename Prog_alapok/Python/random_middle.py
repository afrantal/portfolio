import random

def genRandom():
	list = []
	for i in range(0,5):
		number = random.randint(1,45)
		list.append(number)
	result = calcMiddle(list)
	print('Az átlag: {:<10.3f}'.format(result))

def calcMiddle(list):
	result = 0
	counter = 0
	for i in list:
		result += i
		counter += 1
	result = result / counter
	return result

genRandom()
