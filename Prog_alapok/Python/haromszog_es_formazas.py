#text01 = "Linus"
#text02 = "Torvalds"
#name = text01 + " " + text02
#print(name)
#
#name = "     Linus Torvalds     "
#print(name)
#print("_" + name.lstrip()+ "_")
#print("_" + name.rstrip()+ "_")
#print(name.lstrip().rstrip())
#print(name.strip())
#
#text1 = "Szeretem a tejet"
#print(text1.startswith("Sze"))
#print(text1.endswith("et"))
#print(text1.find("tej"))
#
#person01 = "Linus Torvalds"
#person02 = "Bill Gates"
#person03 = "Steve Jobs"
#
#print(person01 + " | " + person02 + " | " + person03)
#print(person01 , person02 , person03, sep = " | ")

"""
person = "{name} {age}"
print(person.format(name="Linus", age=45))

name="Linus"
age=45
print("{} {}".format( name, age))
"""

"""
number01 = 2.56783456
number02 = 5.123987

print("{} {}".format(number01,number02))
print("{:<20} {:<20}".format(number01,number02))
print("{:20.3} {:20.3}".format(number01,number02))
print("{:020.3} {:020.3}".format(number01,number02))
print("{:020.3f} {:020.3f}".format(number01,number02))
print("{:+20.3} {:+20.3}".format(number01,number02))
print("{:^+20.3} {:^+20.3}".format(number01,number02))  #középre igazítva


name="Linus"
age=45
print(f"{name}'s age is {age}")

text = "Szeretem a tejet"
print(text)
print(text.replace("tejet","sört"))
print(len(text))

print(text[0:5])
print(text[:5])
print(text[-3:])
"""


import math

check = True

while check == True:  #while check:
	a = float(input("A oldal: "))
	b = float(input("B oldal: "))
	c = float(input("C oldal: "))
	if a+b>c and a+c>b and b+c>a:
		s = (a+b+c)/2
		t = math.sqrt(s*(s-a)*(s-b)*(s-c))
		k = a + b + c
		print("A háromszög területe: "+str(t))
		print("A háromszög kerülete: "+str(k))
		check = False
	else:
		print("A háromszög nem szerkeszthető, add meg újra az oldalakat!")


		

