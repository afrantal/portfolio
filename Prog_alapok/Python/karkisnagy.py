#Frantal Attila, 2020.10.31. , esti Szoft
feladat="""
Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 0717
Írjon programot, amely bemenetként karaktereket vár.
Mindaddig fogadja el a bevitelt amíg a bevitt karakter az angol ábécé betűje. 
A program írja ki, hány kis és hány nagybetű volt.
"""
print(feladat)

from string import *

betu = "a"
kisbetu = 0
nagybetu = 0
#lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lista=ascii_lowercase

while str.lower(betu) in lista:
	betu = input("betű = ")
	if str.lower(betu) in lista:
		if betu == str.lower(betu):
			kisbetu += 1
		else:
			nagybetu += 1
	else:
		print("\nAz utolsó karakter nem az angol ABC betűje, ezzel vége a bekérésnek.\n")

print(str(kisbetu)+" db kisbetű, és "+str(nagybetu)+" db nagybetű volt.")
