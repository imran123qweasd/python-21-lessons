"==================loops================"
# циклы - это блок кода, который повторяется несколько раз
# while(до тех пор, пока что) - цикл, который работает до тех пор, пока условие верное
# for - цикл, который работает с итерируемыми объектами. цикл заканчивает свою работу,
# когда он дошел до последнего элемента в итерируемом объекте 

from this import d


count = 10
# while count != 0:
#     print(count)
#     count = count - 1
# print('end')
# # 10,9,8,7,6,5,4,3,2,1,end

# a = 0 # (потому что bool(a) (булевое значение) у 0 это False)
# while a:
#     print('hello')
# # не отработает вообще

# a = '' # (потому что bool(a) (булевое значение) у ''(пустота) это False)
# while a:
#     print('hello')
# # не отработает вообще

# for i in [1,2,3]:
#     print(i)
# # 1,2,3

# for i in range(5):
#     print(i)
# # 0,1,2,3,4

# for i in range(1, 10):
#     print(i)
# # 1,2,3,4,5,6,7,8,9

# for i in 12345:
#     print(i)
# # TypeError

# num = 12345678
# sum = 0
# for i in str(i):
#     sum = sum + int(i)
# print(sum) #36

# string = 'hello'
# for i in string:
#     print(i)

# string = 'hello'
# string2 = 'world123'
# for i in range(len(string)):
#     print(i, string[i], string2[i])
# 0 h w
# 1 e o
# 2 l r
# 3 l l
# 4 o d

# for i in []:
#     print (i)
# # не отработает вообще, потому что нет элементов

# list_ = [1,2,3]
# for i in list_:
#     print(i)
#     list_.append(4) # или строку .append('hello'), любое значение
# # бесконечный цикл for

# string = 'hello'
# for i in string:
#     print(i)
#     string = string + 'hello'
#     print(string)
# отработает только 5 раз, потому что у переменной string ссылка на 70 строке менялась, 
# а у цикла на 68 строке нет

"=========================Ключевые слова в циклах====================="
# break - полностью выйти из цикла
# continue - перейти к следующей итерации

'''for i in range(10):
    if i == 3:
        break
    print(i) 
# 0 1 2

for i in range(10):
    print(i) 
    if i == 3:
        break
# 0 1 2 3

for i in range(10):
    print(i)
    if i == 3:
        continue 
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    if i == 3:
        continue
    print(i) 
# 0 1 2 4 5 6 7 8 9

for i in range(10):
    if i < 3:
        continue
    print(i) 
# 3 4 5 6 7 8 9

list_ = [2,3,4,5,2,4,6,2,2,4,5]
while 2 in list_:
    list_.remove(2)
print(list)'''

'=============================================итерирование сдлваоей===================='
# при итерации словаря , мы будем получать его ключи
dict_ = {'a':1,'z':2,'x':3,'c':4}
'''for key in dict_:
    print(key)'''
dict_ = {'a':1,'z':2,'x':3,'c':4}
for key in dict.keys():
    print(key)
    
