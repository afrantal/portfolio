class Tulajdonsag:
	def __init__(self,ind,nev,magassag,tomeg):
		self.ind = ind
		self.nev = nev
		self.magassag = magassag
		self.tomeg = tomeg

lista = open('test.txt', 'r', encoding="utf-8").read().splitlines()  #szöveges file sorait listába tárolja el

class Kover:
	def sulyos(self):
		print('Túlsúlyos nők:')
		for sor in lista[1:]:
			(ind,nev,magassag,tomeg) = sor.split(';')
			no = Tulajdonsag(ind,nev,magassag,tomeg)
			if int(no.tomeg) > 80:
				print('Név:',no.nev, 'Tömeg:', no.tomeg, 'kg')

	def magas(self):
		f = open('magas_nok.txt','w',encoding="utf-8")
		print('Magas nők:')
		for sor in lista[1:]:
			(ind,nev,magassag,tomeg) = sor.split(';')
			no = Tulajdonsag(ind,nev,magassag,tomeg)
			if int(no.magassag) > 165:
				print('Név:',no.nev, 'Magasság:', no.magassag, 'cm')
				f.write(no.nev + ' , ' + no.magassag + ' cm\n')
		f.close()

neni=Kover()  #a "neni" a Kover osztály egy objektuma
neni.sulyos()
print('--------------------------------------------------')
neni.magas()

