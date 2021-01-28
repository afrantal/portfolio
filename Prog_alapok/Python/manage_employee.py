from employee import Employee
from datetime import *

class ManageEmployee:
	def __init__(self):
		self.rowList = []
		self.readFile()
		self.countEmployee()
		self.sumMiskolcSal()
		self.szegedWrite()
		self.miski()
		self.miskolc()
		self.younger()

	def readFile(self):
		print("Első feladat: fájl beolvasás.")
		file = open("dolgozok100.txt","r",encoding = "utf-8")
		file.readline()  #első sor kiolvasása, ez a fejléc, ezért itt olvassuk ki és nem teszzük a listába
		row = file.readline() 
		while row:
			rowS = row.split(":")
			emp = Employee()
			emp.name = rowS[0]
			emp.city = rowS[1]
			emp.address = rowS[2]
			emp.salary = rowS[3]
			emp.bonus = rowS[4]
			emp.borndate = rowS[5]
			emp.hiredate = rowS[6]
			
			self.rowList.append(emp)
			row = file.readline()
		
		file.close()
		print("Sikeres beolvasás")

	def countEmployee(self):
		print('\nMásodik feladat: Dolgozók megszámlálása')
		counter = 0
		for i in self.rowList:
			counter += 1
		print("A dolgozók száma: {:10}".format(counter))

	def sumMiskolcSal(self):
		print("\nHarmadik feladat: miskolci fizetések összegzése")
		sumSalary = 0
		for i in self.rowList:
			if i.city == "Miskolc":
				sumSalary += int(i.salary)
		print("A miskolciak össz fizetése:", sumSalary)

	def szegedWrite(self):
		print("\nNegyedik feladat: szegedi fizetések file-ba írása")
		sumSalary = 0
		for i in self.rowList:
			if i.city == "Szeged":
				sumSalary += int(i.salary)
		wFile = open("szegedi.txt","w", encoding = "utf-8")
		wFile.write("A szegediek fizetése: " + str(sumSalary))
		wFile.close()
		print("Sikeres kiírás")

	def miski(self):
		print("\nÖtödik feladat: Miskolciak kiíratása")
		for i in self.rowList:
			if i.city == "Miskolc":
				print(i.name,',',i.city,',',i.address)

	def miskolc(self):
		print("\nHatodik feladat: Miskolciak file-ba írása")
		m = open("miskolci.txt","w", encoding="utf-8")
		for i in self.rowList:
			if i.city.lower() == "miskolc":
				m.write(i.name+'\n')
		print("Sikeres kiírás")
		m.close()

	def younger(self):
		print("\nHetedik feladat: legfiatalabb dolgozó(k) ")
		minage = datetime.fromisoformat(self.rowList[0].borndate)
		for i in self.rowList:
			if datetime.fromisoformat(i.borndate) < minage:
				minage = datetime.fromisoformat(i.borndate)

		for i in self.rowList:
			if datetime.fromisoformat(i.borndate) == minage:
				print(i.name, i.borndate)

ManageEmployee()
