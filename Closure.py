print()
# PRZYKŁAD 1 -------------------------------------------------------------------
print('PRZYKŁAD 1'.center(85,'-'))
def outer(par):
	lok = par
	def inner():
		return lok
	return inner

zm = 1
fun = outer(zm)
print(fun())

print()
# PRZYKŁAD 2 -------------------------------------------------------------------
print('PRZYKŁAD 2'.center(85,'-'))
def domknij(par):
	loc = par
	def potega(p):
		return p ** loc
	return potega

fsqr = domknij(2)
fcub = domknij(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))

print()
# PRZYKŁAD 3 -------------------------------------------------------------------
print('PRZYKŁAD 3'.center(85,'-'))
def mnozenie_przez(mnoznik):
	def domnoz(mnozna):
		# funkcja wykorzystuje dwie zmienne:
		# mnozna - dostępną dla użytkownika
		# mnoznik - zdefiniowaną tylko wewnątrz funkcji 'mnozenie_przez'
		return mnozna * mnoznik

	return domnoz

iloczyn_5_przez = mnozenie_przez(5)

print(iloczyn_5_przez(12))	# zostanie wypisane 12*5, czyli 60
