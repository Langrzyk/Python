from os import strerror

name = input("Enter the name of the text file: ")

if name[-4:] == '.txt':
    path = 'data/' + name
    pathfile = 'data/' + name[:-4] + "_hist" + '.txt'
else:
    path = 'data/' + name + '.txt'
    pathfile = 'data/' + name + "_hist" + '.txt'

dict = {}
try:
    #read
    for line in open(path, "rt"):
        for i in list(line.lower())[:-1]:
            if ord(i) >= 97 and ord(i) <= 122:
                if not i in dict.keys():
                    dict[i] = 1
                else:
                    dict[i] += 1
            else:
                continue

    print("\nWYSTĘPOWANIE ZNAKÓW")
    for key in sorted(dict):
        print(key, "->", dict[key], end="  ")

    print("\nHISTOGRAM ZNAKOW")
    sorted_x = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    for i in sorted_x:
        print(i[0], "->", i[1], end="  ")

    #write
    file = open(pathfile,'wt')
    for i in sorted_x:
        file.write(str(i[0]) + "->" + str(i[1]) + "  ")
    file.close()
    print()

except IOError as e:
    print("".center(68,'_'))
    print("ERROR I/O: ", strerror(e.errno))
else:
    print("".center(68,'_'))
    print("everything went well".upper().center(26,"-"))
finally:
    print()
    print("Author: Betina Langrzyk")
    print("Date: 20/04/2020")
    print("Page: https://github.com/Langrzyk")
