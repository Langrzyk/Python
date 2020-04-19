class PizzaError(Exception):
    def __init__(self, pizza='nieznana', wiadomosc=""):
        Exception.__init__(self, wiadomosc)
        self.pizza = pizza


class ZaDuzoSeraError(PizzaError):
    def __init__(self, pizza='nieznana', ser='>100', wiadomosc=""):
        #PizzaError.__init__(self, pizza, wiadomosc)
        super().__init__(pizza, wiadomosc)
        self.ser = ser


def zrobPizze(pizza, ser):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError
	if ser > 100:
		raise ZaDuzoSeraError
	print("Pizza gotowa!")


for (pz, s) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		zrobPizze(pz, s)
	except ZaDuzoSeraError as tmce:
		print(tmce, ':', tmce.ser)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)
