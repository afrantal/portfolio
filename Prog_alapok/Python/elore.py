feladat="""Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 1006:
Kérjen be két karaktert, írassa ki, melyik van előrébb az ábécében.
"""
print(feladat)
print("--------------------------------------------------------------------------------------------------\n")

from string import *
print(ascii_letters)

betu1 = input("Adj meg egy betűt: ")
betu2 = input("Adj meg egy másik betűt: ")

if str.lower(betu1) < str.lower(betu2):
	print("\n\""+betu1+"\"", "előrébb van az ábécében.")
elif str.lower(betu1) > str.lower(betu2):
	print("\n\""+betu2+"\"", "előrébb van az ábécében.")
