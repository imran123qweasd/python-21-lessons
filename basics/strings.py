"================Строки=================="
# строки - не изменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки
# Синтаксис:
from asyncio import SendfileNotAvailableError
from itertools import count
from re import T
from winreg import HKEY_LOCAL_MACHINE


string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error = 'не правильная строка"
string3 = "Don't" # внутри двойных кавычек все одинарные - просто символы
string4 = '"Makers bootcamp"' # внутри одинарных кавычек все двойные - просто символы

string5 = '''
Многострочный текст 
в одинарных кавычках
Тут можно ставить "любые" 'кавычки'
"""""
'''
string6 = """
Многострочный текст 
в двойных кавычках
Тут можно ставить "любые" 'кавычки'
'''''
"""

"================Экранизация Строк=================="
# спекс символы
'\n' #перенос на новую строку
hello 
worrld
'\t' #табуляция
'\\' # отображение слеша потосу что он инструкСией для питона
'\'' # отображение ковычки
'\r' # возвращение каретки в начало строкиэ
print('my wevsite is latracal \r solutin')
# solutionte is latracal
'\v' # под конец слова он перемещает 2 слово на новую строку вниз под конец первого 
print('''hellow \v
               world ''')

"================Форматирование Строк=================="
title = 'pilow'
price = 1500
format1 = f'Название: , {title}, Ценa: {price}'

format2 = 'Название : %s, Цена: %s'
print(format2 %("gulyash", "40"))

format3 ='еазвание :{}, цена: {}'
orint(format3.format('шакарап', '35'))

"================Метода стркотр]ок========/==========3"
 
 #методы типы данных это функции к которым мы обращаемся через точку
 # dir(str) # пишем дир и в скобках то что зотим узнать о нем(посмотреть все методы и класса) 
 
 'HELLO'. lower() # 'hello'
 'lapuh'. upper() # 'LAPUH'
 'HelLo'. swapcase()# 'hELlO'
 'helli'. title()# Hello
 'Hello World'.capitalize() # Hello world
 'hellow coint',count('l') x2
 'helllllowwwww'.count('w') x5
 'gello world'.startswith('hell') #false]
 'hello world'.startswith('hell') #true]




a = 4
b = 5
c, d = 6, 7
b, a = a, b
(magic)







 "================индексты========/==========3"
 # это порядковый номер символа в строке

 'H e l l o   w o r l d'
 #0 1 2 3 4 5 6 7 8 9 10
string = ' Hello woeld'
string[0]#H
string[5]# 
string[6]#w
string[2]#l
string[1]#e
string[4]#o

# срезы - это подстрока строки
string[0:5] #hello
string[0:8] #hello wo
string[2:4] #Ll
string[4:5][3:5] ow ,     
string[0:11:2]# hlowrd
string[::3] # hlwl
string[::-1] # dlrow olleh
string[ ::-2]# drwolh

'hello workd'.find(wo)# 7,8
'hello world'.split() # ['hello''world')
'$'.join(['hellow ', 'world']) # hello$world


# конкатенация - склеивание стjr







a = 5
b = 5
print(id(a))
print(id(b))



