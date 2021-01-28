from employee import Employee
from datetime import *

class dolg:
	def __init__(self):
		self.dolgozok = []
		self.betoltes()
		self.nagysag()


	def betoltes(self):
		print("A file beolvasása lista változóba.")
		file = open("dolgozok100.txt","r",encoding="utf-8")
		file.readline()
		sor = file.readline()
		while sor:
			sp_sor = sor.split(":")
			tmp = Employee()
			
			tmp.name = sp_sor[0]
			tmp.city = sp_sor[1]
			tmp.address = sp_sor[2]
			tmp.salary = sp_sor[3]
			tmp.bonus = sp_sor[4]
			tmp.borndate = sp_sor[5]
			tmp.hiredate = sp_sor[6]
			
			self.dolgozok.append(tmp)
			sor = file.readline()

		file.close()
		print("Sikeres beolvasás.")

	def nagysag(self):
		counter = 0
		for i in self.dolgozok:
			counter += 1
		print("\nA belvasott file {} soros.".format(counter))
				


dolg()
