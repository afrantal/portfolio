from employee import Employee

class manage:
	def __init__(self):
		self.L = []
		self.belolvas()
		self.miskolc()
		self.little_salary()

	def belolvas(self):
		f = open("dolgozok100.txt","r", encoding="utf-8")
		f.readline()
		r = f.readline()
		while r:
			row = r.split(":")
			tmp = Employee()
			tmp.name = row[0]
			tmp.city = row[1]
			tmp.address = row[2]
			tmp.salary = row[3]
			tmp.bonus = row[4]
			tmp.borndate = row[5]
			tmp.hiredate = row[6]
			
			self.L.append(tmp)
			r = f.readline()
		f.close()

	def miskolc(self):
		print("Miskolciak:")
		m = open("miskolci.txt","w", encoding="utf-8")
		for i in self.L:
			if i.city.lower() == "miskolc":
				print(i.name)
				m.write(i.name+'\n')
		m.close()

	def little_salary(self):
		print("\nLegkisebb fizetésűek:")
		min_sel = int(self.L[0].salary)
		for i in self.L:
			if int(i.salary) <  min_sel:
				min_sel = int(i.salary)
		
		for i in self.L:
			if min_sel == int(i.salary):
				print("Név:",i.name,", Város:", i.city,", Fizetés:", min_sel)


manage()
