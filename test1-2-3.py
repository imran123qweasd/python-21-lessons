'''
#task 1

1) Напишите программу, которая просит пользователя ввести последовательно день своего рождения, 
затем месяц и в конце год рождения.
На выходе программа должна выдавать вам сумму введенных чисел.



a = int(input('Введите свой день рождение!:'))

b = int(input('Введите свой месяц рождения!:'))

c = int(input('Введите свой год рождения!::'))

print( a + b +c )
#я чуток запутался C int ,подсказали и допер, 




#task 3

Найдите площадь и длину круга по введенным пользователем данным. 
Округлите полученные числа до сотых (два знака после точки)

from math import pi

r = float(input("введите радиус круга:"))

print ("площадь круга C радиусом: " + str(r) + " это: " + str(pi * r**2))

# r это радиус круга, sstr строка,pi число ПИ   , PI я импортировал с math( инет помог ), и возвел в степеннь

#task2

римечание: при вводе не надо указывать знак %

Пример:
Ввод: Введите скидку: 7
Вывод: Оставшаяся сумма для платежа составляет 558$


from calendar import c

'''
price = float(600)

discent = float(input("Введите скидку:"))

print('Оставшаяся сумму для платежа составляет',abs( price*discent/100-price))

'''
from os import makedirs
'''

