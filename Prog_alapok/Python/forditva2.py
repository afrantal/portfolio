a = list(input("Adj meg egy karakter sorozatot: "))
e = ''

for i in range(1, len(a)+1):
	e += a[-1*i]

print(e)
