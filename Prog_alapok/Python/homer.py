#Frantal Attila, 2020.10.31., esti Szoft
feladat="""Frantal Attila, 2020.10.31., esti Szoft\n
Feladat 0735:
Írjon programot, amely a következő hőmérséklet adatokat, valós számok alakjában tárolja:

15,82
18,27
22,40
23,19
24,57
22,02
20,28
A program készítsen egy vízszintes irányú grafikont, amelyen ábrázolja a 7 nap adatait.

A sorok a hőmérséklet adat értéket mutassák először, 1 tizedesjegy pontossággal, 5 szélesen. ezt kövesse a grafikon adott oszlopa. Legyen fejléc.

Példa:

fok |0        10        20       30
15.8 ###############
18.2 ##################
22.4 ######################
23.1 #######################
24.5 ########################
22.0 ######################
20.2 ####################
"""
print(feladat)

import math

lista = [15.82,18.27,22.40,23.19,24.57,22.02,20.28]

print('--------------eredmény--------------\n')
print('fok |0        10        20       30')
for i in range(0,len(lista)):
	print(('{:<5.1f}'.format(lista[i])) + ' ' + '#'*math.floor(lista[i]))
