#Frantal Attila, 2020.10.31. , esti Szoft
feladat="""
Frantal Attila, 2020.10.31. , esti Szoft\n
Feladat 0715:
Írassa ki az angol ábécé nagybetűit. A program első sora saját nevét, osztályát és a mai dátumot tartalmazza.
"""
print(feladat)
from string import *

print(ascii_uppercase) #egy sorban

print() #üres sor
#egymás alá
for i in range(0,len(ascii_uppercase)):
	print(ascii_uppercase[i])
