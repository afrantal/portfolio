print("Frantal Attila, 2020.10.01\n")


kor = int(input('Válasszon: 1. csecsemő, 2. pubertás, 3. sportoló, 4. 50 év feletti, 0. egyik sem \n'))
tomeg = int(input('Testtömeg (kg) = '))
magassag = float(input('Magasság (méter) = '))
hatvany = 2.5

if kor == 1:
	hatvany = 3
elif kor == 2:
	hatvany = 2

bmi = (1.3 * tomeg) / (magassag**hatvany)
print('Testtömegindex', bmi)

if bmi < 16:
	print('súlyos soványság')
elif bmi >= 16 and bmi < 17:
	print('mérsékelt soványság')
elif bmi >= 17 and bmi < 18.5:
	print('enyhe sovány')
elif bmi >= 18.5 and bmi < 25 and kor not in (3,4) or bmi >= 18.5 and bmi < 27 and kor in (3,4):
	print('egészséges')
elif bmi >= 25 and bmi < 30:
	print('túlsúlyos')
elif bmi >= 30 and bmi < 35:
	print('I. fokú elhízás')
elif bmi >= 35 and bmi < 40:
	print('II. fokú elhízás')
elif bmi >= 40:
	print('III. fokú súlyos elhízás')
