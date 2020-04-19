#strumien = open("tzop.txt", "rt", encoding = "utf-8") # otwarcie tzop.txt w trybie do odczytu, zwrocenie go jako obiekt pliku
#print(strumien.read()) # wyswietlenie zawartosci pliku

print()
# ODCZYT CAŁEGO PLIKU NA RAZ ---------------------------------------------------
print('ODCZYT CAŁEGO PLIKU NA RAZ'.center(86,'-'))
from os import strerror

def odczyt1(name):
    try:
        licznik = 0
        s = open('data/'+name, "rt")
        zawartosc = s.read()
        for zn in zawartosc:
            print(zn, end='')
            licznik += 1
        s.close()
        print("\n\Znaki w pliku:", licznik)
    except IOError as e:
        print("Blad I/O: ", strerror(e.errno))

odczyt1('text.txt')

print()
# ODCZYT PLIKU LINIA PO LINII --------------------------------------------------
print('ODCZYT CAŁEGO PLIKU LINIA PO LINII'.center(86,'-'))
from os import strerror

def odczyt2(name):
    try:
        licznikZn = licznikL = 0
        s = open('data/'+name, 'rt')
        linia = s.readline()
        while linia != '':
            licznikL += 1
            for zn in linia:
                print(zn, end='')
                licznikZn += 1
            linia = s.readline()
        s.close()
        print("\n\Znaki w pliku:", licznikZn)
        print("\Linie w pliku:", licznikL)
    except IOError as e:
        print("Blad I/O:", strerror(e.errno))

odczyt2('text.txt')

print()
# ODCZYT CAŁEGO PLIKU ZWROCENIE LISTY LINII PLIKU ------------------------------
print('ODCZYT CAŁEGO PLIKU ZWROCENIE LISTY LINII PLIKU'.center(86,'-'))
from os import strerror

def odczyt3(name):
    try:
        licznikZn = licznikL = 0
        s = open('data/'+name, 'rt')
        linie = s.readlines(20)
        while len(linie) != 0:
            for linia in linie:
                licznikL += 1
                for zn in linia:
                    print(zn, end='')
                    licznikZn += 1
            linie = s.readlines(10)
        s.close()
        print("\n\Znaki w pliku:", licznikZn)
        print("\Linie w pliku:", licznikL)
    except IOError as e:
        print("Blad I/O:", strerror(e.errno))

odczyt3('text.txt')

print()
# ODCZYT PLIKU LINIA PO LINII OBIEKT JAKO INSTANCJA KLASY ITEROWALNEJ ----------
print('ODCZYT PLIKU LINIA PO LINII OBIEKT JAKO INSTANCJA KLASY ITEROWALNEJ'.center(86,'-'))
from os import strerror

def odczyt4(name):
    try:
    	licznikZn = licznikL = 0
    	for linia in open('data/'+name, 'rt'):
    		licznikL += 1
    		for zn in linia:
    			print(zn, end='')
    			licznikZn += 1
    	print("\n\Znaki w pliku:", licznikZn)
    	print("\Linie w pliku:", licznikL)
    except IOError as e:
    	print("Blad I/O: ", strerror(e.errno))

odczyt4("text.txt")

# ZAPIS DO PLIKU Z WCZESNIEJSZYM JEGO UTWORZENIEM ZNAK PO ZNAKU ----------------
print('ZAPIS DO PLIKU Z WCZESNIEJSZYM JEGO UTWORZENIEM ZNAK PO ZNAKU'.center(86,'-'))
from os import strerror

def zapis1(name):
    try:
    	otworzPlik = open('data/'+name, 'wt') # utworono nowy plik (nowytxt.txt)
    	for i in range(10):
    		s = "linia #" + str(i+1) + "\n"
    		for zn in s:
    			otworzPlik.write(zn)
    	otworzPlik.close()
    except IOError as e:
    	print("Blad I/O: ", strerror(e.errno))

zapis1('nowytxt.txt')
odczyt4('nowytxt.txt')

# ZAPIS DO PLIKU Z WCZESNIEJSZYM JEGO UTWORZENIEM LINIA PO LINII ---------------
print('ZAPIS DO PLIKU Z WCZESNIEJSZYM JEGO UTWORZENIEM LINIA PO LINII'.center(86,'-'))
from os import strerror

def zapis2(name):
    try:
    	otworzPlik = open('data/'+name, 'wt')
    	for i in range(10):
    		otworzPlik.write("linia #" + str(i+1) + "\n")
    	otworzPlik.close()
    except IOError as e:
    	print("Blad I/O: ", strerror(e.errno))

zapis2('nowytxt2.txt')
odczyt4('nowytxt2.txt')
