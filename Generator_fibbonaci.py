print()
# wersja obiektowa -------------------------------------------------------------
# bezpośredniej implementacji protokołu iteratora ------------------------------
print('WERSJA OBIEKTOWA'.center(85,'-'))
class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		#print("Fib iter")
		return self

	def __next__(self):
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		#print("Class iter")
		return self.__iter;


for i in Class(10):
	print(i, end=' ')
print()
print(list(Class(10)))



print()
# GENERATOR Z YIELD ------------------------------------------------------------
print('GENERATOR Z YIELD'.center(85,'-'))
def Fibs(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

for i in Fibs(10):
	print(i, end=' ')
print()
print(list(Fibs(10)))


print()
# WYRAŻENIE LISTOWE A GENERATOR
print('WYRAŻENIE LISTOWE A GENERATOR'.center(85,'-'))
lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10))

print(lst)
for v in lst:
    print(v, end=" ")
print()

print(genr)
for v in genr:
    print(v, end=" ")
print()
