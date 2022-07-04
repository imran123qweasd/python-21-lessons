#1) Создайте список, который будет содержать различные типы данных.
#  Напишите программу, которая будет находить корень чисел
#  содержащихся в созданном списке Используйте встроенные функции.
from math import sqrt
list_ = [4, " abc", 3, 12, True, 2.5, False] 
new_list = list(map(lambda x: round (sqrt(x)), filter(lambda y: type(y) == int, list_)))
print(new_list)
num = 4321
if str(num)[0] > str(num)[1] and str(num)[1] > str(num)[2] and str(num)[2] > str(num)[3]:
    print('yes')
else:
        print('no')

