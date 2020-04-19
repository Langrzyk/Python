from os import strerror

dane = bytearray(10)

for i in range(len(dane)):
    dane[i] = 10 + i

# zapis ------------------------------------------------------------------------
try:
    bf = open('data/file.bin', 'wb')
    bf.write(dane)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print()
# odczyt -----------------------------------------------------------------------
print('ODCZYT'.center(86,'-'))
data = bytearray(10)

try:
    bf = open('data/file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Blad I/O:", strerror(e.errno))

print()
# odczyt2 UWAGA NA PAMIĘC!! ----------------------------------------------------
print('ODCZYT UWAGA NA PAMIĘC!!'.center(86,'-'))
from os import strerror

try:
    bf = open('data/file.bin', 'rb')
    dane = bytearray(bf.read())
    bf.close()

    for b in dane:
        print(hex(b), end=' ')

except IOError as e:
    print("Blad I/O:", strerror(e.errno))

print()
# odczyt3 TYLKO 5 PIERWSZYCH BAJTOW!! ------------------------------------------
print('ODCZYTTYLKO 5 PIERWSZYCH BAJTOW!!'.center(86,'-'))
data = bytearray(10)
try:
    bf = open('data/file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Blad I/O:", strerr(e.errno))

print()
# KOPIUJE PLIK BINARNY DO 2 PLIKU BINARNEGO ------------------------------------------
print('KOPIUJE PLIK BINARNY DO 2 PLIKU BINARNEGO'.center(86,'-'))
from os import strerror

nazwaZrodla = 'file.bin'
try:
    src = open('data/'+nazwaZrodla, 'rb')
except IOError as e:
    print("Nie mozna otworzyc pliku zrodlowego: ", strerror(e.errno))
    exit(e.errno)

nazwaDocelowa = 'file2.bin'
try:
    dst = open('data/'+nazwaDocelowa, 'wb')
except Exception as e:
    print("Nie mozna utworzyc pliku docelowego: ", strerror(e.errno))
    dst.close()
    exit(e.errno)

bufor = bytearray(65536)
suma  = 0
try:
    wczytany = src.readinto(bufor)
    while wczytany > 0:
        zapisany = dst.write(bufor[:wczytany])
        suma += zapisany
        wczytany = src.readinto(bufor)
except IOError as e:
    print("Nie mozna utworzyc pliku docelowego: ", strerror(e.errno))
    exit(e.errno)

print(suma,'bajt(y) poprawie zapisany')
src.close()
dst.close()
