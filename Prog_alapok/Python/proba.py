print("Készítette: Frantal Attila , 2020.09.30")

#a=None
#while a!=0:
#	a = int(input("szám: ")) #0-val ki tudok szállni
#	print("Ezt írtad", a)

#a=None
#b=0
#
#while a!=0:
#	a = int(input("szám: ")) #0-val ki tudok szállni
#	b += a
#
#print("Az összeg", b)


#a=None
#b=1
#
#while a!=0:
#	a = int(input("szám: ")) #0-val ki tudok szállni
#	if(a!=0):
#		b *= a
#
#print("Az összeg", b)



number=None
less = 100
biggest = 1

while number != 0 :
	number = int(input("szám: ")) #0-val ki tudok szállni
	if(number < less):
		if number != 0:
			less = number
	if(number > biggest):
		if number != 0:
			biggest = number

print("Minimum: ", less, "Maximum: ", biggest)


#a = int(input("szam: "))
#
#if (a%2==0) and (a%3==0):
#	print("Mindkettővel oszható")
#else:
#	print("Osztható 2-vel vagy 3-mal.")
#
#if (a%2==0) or (a%3==0):
#	print("Valamelyikkel oszható")
#else:
#	print("egyikkel sem osztható")


#a=4
#b=6
#
#if (a<b) and (a%2==0) and (b%3==0):
#	print("A feltételek igazat adtak.")
#else:
#	print("Nem voltak igazak a feltételek.")

#a=5
#b=3
#
#if (a<b) or (a%2==0):
#	print("Valamelyik feltétel igaz.")
#else:
#	print("A feltételek hamisak.")

#a = None

#a = int(input("Szám: "))
