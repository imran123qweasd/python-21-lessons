'''a = float(input('Введите первое число!  '))
b = float(input('Введите второе число!  '))
c = input('введите +, -, *, /: ')
if c == "+":
   print(a + b)
if c == "-":
   print(a - b)     
    
if c == "*":
   print(a * b)
   
if c == "/":
   print(a / b)

a = float(input('Введите первое число!  '))
b = float(input('Введите второе число!  '))
c = '{1}, {2}, {3}, {4}'.format('+', '-', '*', '/') 
if c == "1":
   print(a + b)
if c == "2":
   print(a - b)     
    
if c == "3":
   print(a * b)
   
if c == "4":
   print(a / b)



1) Напишите программу, которая будет запрашивать пользовательские данные: имя, фамилию, возраст. 
Далее программа должна проделать следующие операции: в имени убрать все буквы ‘a’(если они есть),
 в фамилии - разделить все буквы разделителем *. В конце программа выдает вам объединенную строку, 
 состоящую из полученных имени и фамилии, при этом данная строка должна повторяться столько раз,
  сколько составляет возраст пользователя.

Например:
Ввод: Введите имя, фамилию и возраст через пробел: John Snow 4
Вывод: JоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*w

'''
data = (input('Введите имя, фамилию и возраст через пробел:').split())
name =data[0]
last_time = data[1]
age = data[-1]

name = name.lower().replace('a', '')
last_time = '*'.join(list(last_time))
print((name + last_time) * int(age))


'''
2) Напишите программу, которая высчитывает количество гласных букв в введенной пользователем строке. 
И программа выдает вам следующее предложение: В вашей строке насчитано n гласных букв.

Например:
Ввод: Введите строку: I love Makers Bootcamp!
Вывод: В вашей строке насчитано 8 гласных букв

3) Напишите программу, которая просит пользователя ввести свой юзернейм (одним словом) и генерирует пароль из юзернейма,
 добавив в конец строки символ $, в середину символ &, и заменив строчные буквы на заглавные и наоборот.

Например:
Ввод: Введите юзернейм: JohnSnow
Вывод: Вам сгенерирован пароль: jOHN&sNOW$
'''