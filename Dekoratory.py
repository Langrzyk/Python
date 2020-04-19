from functools import wraps

# dekorator ZAMAIAST
print("\n-------------------------DEKORATOR ZAMIAST---------------------------")
def blocker(to_be_blocked):
    def pint_blocker_msg():
        print(f'Blocked: {to_be_blocked.__name__}')
    return pint_blocker_msg

@blocker
def play_music():
    print('Music plays')

play_music()


#dekorator pezed i po
print("\n-------------------------DEKORATOR PRZED I PO------------------------")
def wrapper(callable):
    @wraps(callable)
    def inner():
        print(f'Dzieję się przed {callable.__name__}')
        val = callable()
        print(f'Dzieję się po {callable.__name__}')
        return val
    return inner

@wrapper
def say_hello():
    print('hello')

say_hello()

print(say_hello.__name__)

#funkcja z argumentami
print("\n-------------------------FUNKCJA Z ARGUMENTAMI-----------------------")
from functools import wraps

def bumelant(szybka_funkcja):
    @wraps(szybka_funkcja)
    def inner(*args, **kwargs):
        result = szybka_funkcja(*args, **kwargs)
        print('Zasada zachowania energii: zachowaj energię na później :)')
        return result
    return inner


@bumelant
def play(music='polskie regge'):
    print('Gra: {}'.format(music))

play()
play('jazz')



#Argumenty dekoratora
print("\n-------------------------ARGUMENTY DEKORATORA------------------------")
from functools import wraps

def bumelant(sentence):
    print('decorator called with sentence:', sentence)
    def real_decorator(to_be_decorated):
        @wraps(to_be_decorated)
        def wrapper(*args, **kwargs):
            result = to_be_decorated(*args, **kwargs)
            print('Zasada zachowania energii: zachowaj energię na później :)')
            print('Sentencja dekoratora:', sentence)
            return result
        return wrapper
    return real_decorator


@bumelant('Co masz zrobić dziś zrób pojutrze, będziesz mieć 2 dni wolnego')
def play(music):
    print('Gra: {}'.format(music))

play('song of victory')
print(play.__name__)


#własny wraps
print("\n-------------------------WŁASNY WRAPS--------------------------------")
def my_wraps(original):
    def outer_wrapper(to_be_decorated):
        def wrapper(*args, **kwargs):
            return to_be_decorated(*args, **kwargs)
        wrapper.__name__ = original.__name__
        return wrapper
    return outer_wrapper

def przodownik(wolna_funkcja):
    @my_wraps(wolna_funkcja)
    def inner(*args, **kwargs):
        print('Pierwszy!!!!')
        return wolna_funkcja(*args, **kwargs)
    return inner

@przodownik
def play(music):
    print('Gra: {}'.format(music))

play('disco')
print(play.__name__)
