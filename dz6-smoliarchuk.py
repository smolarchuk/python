#Написать программу перевода числа из арабских цифр в число из римских цифр.Написать программу обратного перевода.

CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

def arab_to_roman(number):
    if number <= 0: return ''

    ret = ''
    for arab, roman in CONV_TABLE:
        while number >= arab:
            ret += roman
            number -= arab

    return ret

def roman_to_arab(txt):
    txt = txt.upper()
    ret = 0
    for arab, roman in CONV_TABLE:
        while txt.startswith(roman):
            ret += arab
            txt = txt[len(roman):]
    return ret


for i in ( 0, 4, 8, 9, 31, 46, 99, 583, 888, 1668, 1989, 2009, 2010, 2011, 3999 ):
    arab = arab_to_roman(i)
    roman = roman_to_arab(arab)
    if __name__ == "__main__":
        print(i, arab, roman)


# Написать функцию no_numbers которая удаляет из файла все цифры. Функция должна принимать путь к файлу.

import re

def no_numbers(text):
    pattern = '[0-9]'
    text = [re.sub(pattern, '', i) for i in text]
    return ''.join(text)

f = open("input_file.txt","r")
text = f.readlines()
print(no_numbers(text))
with open("input_file.txt",'w') as F:
    F.writelines(no_numbers(text))



# Написать функцию реализующую шифрование Цезаря. Функция принимает 2 параметра, текст и сдвиг, возвращает зашифрованный текст. Написать функцию реализующую дешифровку Цезаря.

llst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
blst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

msg = input("Message: ")
shift = int(input("Shift: "))

def encryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)%len(llst)
            ret += llst[(ind+shift)%len(llst)]
        elif x in blst:
            ind = blst.index(x)%len(llst)
            ret += blst[(ind+shift)%len(llst)]
        else:
            ret += x
    return ret

def decryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind-shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind-shift]
        else:
            ret += x
    return ret

print(encryptCaesar(msg, shift))
print(decryptCaesar(msg, shift))


# Зашифровать данные в файле шифрованием Цезаря и записать в новый файл.

llst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
blst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

data = open("input_file.txt", "r")
msg = data.readline()
print(msg)
shift = int(input("Shift: "))

def encryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)%len(llst)
            ret += llst[(ind+shift)%len(llst)]
        elif x in blst:
            ind = blst.index(x)%len(llst)
            ret += blst[(ind+shift)%len(llst)]
        else:
            ret += x
    return ret

with open("output_file.txt","w") as ex:
    ex.writelines(encryptCaesar(msg, shift))

print(encryptCaesar(msg, shift))

