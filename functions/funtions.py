"===================Функции======================"
# функция - именнованный блок кода, который может принимать аргументы и возвращать результат

def my_sum(a, b):
    return a + b

res = my_sum(5,4)
print(res) # 9


"==================Параметры===================="
# параметры - локальные переменные внутри функции, значения которым мы задаем при вызове функции (переменные, которые мы указали внутри скобочек при создании функции (когда написали def))
# сначала определяем обязательные, потом с дефолтом, потом *, и в конце **

"===========Виды параметров============="
# 1. обязательные
# 2. необязательные
# 2.1 по дефолту (со значением по умолчанию) (обьявляем переменную чо значением через =)
# 2.2 args
# 2.3 kwargs


"==================Аргументы===================="
# аргументы - значения, которые мы передаем параметрам при вызове функции
# сначала всегда передаются позиционные потом именованные

"============Виды аргументов============="
# 1. позиционные
# 2. именованные (ключ=значение)


def sum_or_add_10(a, b=10):
    # b - параметр с дефолтом 10
    return a + b

print(sum_or_add_10(2,3)) # 5
print(sum_or_add_10(5)) # 15
print(sum_or_add_10(2,9)) # 11
print(sum_or_add_10(15)) # 25

def func(*args, **kwargs):
    """
    args - tuple, в который нам приходят все аргументы, которые были переданы через запятую (кроме обязательных и по дефолту)
    kwargs - dict, в который нам приходят все аргументы, которые были переданы ввиде ключ=значение (кроме именованных) 
    """
    print("args -", args)
    print("kwargs -", kwargs)

func(1,2,3,4,5,(56,6,7,8,8,9,0),{"a":5}, a=3, b=5)

def func2(a, b=5, *c, **d):
    print("a -", a)
    print("b -", b)
    print("c -", c)
    print("d -", d)

# func2()   - TypeError: func2() missing 1 required positional argument: 'a'

func2(10)
# a - 10
# b - 5
# c - ()
# d - {}

func2(10,20)
# a - 10
# b - 20
# c - ()
# d - {}

func2(10,20,30,40)
# a - 10
# b - 20
# c - (30, 40)
# d - {}

func2(b=20, a=10)
# a - 10
# b - 20
# c - ()
# d - {}

# func2(10,20,30,40,a=5,b=6)   # TypeError: func2() got multiple values for argument 'a'
# потому что в переменную a позиционно мы передали 10, а именованно 5

func2(10,20, 30, 40, c=5, d=6)
# a - 10
# b - 20
# c - (30, 40)
# d - {'c': 5, 'd': 6}


"==================*===================="
# * - знак умножения
# * - распаковка

list_ = [1,2,3,4,5]
list2 = [*list_] # распаковываем значения в списке в новый список

dict_ = {'a':3, 'b':6}
dict2 = {**dict_} # распаковываем пары в словаре в новый словарь


def aigerim():
    print("Несу маркер")
    return "marker"

def nastya():
    print("Айгерим, принеси пожалуйста маркер")
    marker = aigerim()
    print("Айгерим принесла", marker)

nastya()


len( [1,2,3] ) # 3

def my_len(obj):
    count = 0
    for i in obj:
        count = count + 1
    return count

print(my_len([1,2,3,4,5])) # 5
print(my_len('sdfghjkl')) # 8



database = {
    "Бекзат": "скала",
    "Эртай": "пароль",
    "Оомат": "Кыргызстан",
    "Имран": "12345",
    "Жийде": "return",
    "Манас": "Маке",
    "Арафат": "54321",
    "Элжаз": "парол",
    "Гулсана": "312",
    "Эркайым": "Айдин",
    "Бекназ": "Арёль",
    "Эдиль": "ьлорап",
    "Айгул": "май",
    "Закир": "@@@",
    "Бегайым": "makers",
    "Мырзайым": "Bootcamp2221",
    "Даниэл": "covid19",
    "Жибек": "1404",
    "Айгерим":"moon02",
    "Калысбек": "стол",
    "Ырыс": "suuuuuuuuiiiiiiiiiiii",
    "Айканыш": "qwerty",
    "Арген": "11172332",
    "Нурмухамед": "Не верный",
    "Бектур": "0101",
    "Алан": "душу питона",
    "Жаангер": "ох блин",
    "Богдан": "Кудайберген",
    "Айгерим": "синий маркер",
    "Настя": "Python21"
}

def login(username):
    for i in range(3):
        if username in database:
            password = input("Введите пароль: ")
            if password == database[username]:
                print("Success")
                break
            else:
                print("Incorrect password")
        else:
            print("Incorrect username")
            break

login(username="Мырзайым")


def translate(string):
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"    
    if string[0] in eng:
        dictionary = str.maketrans(eng, ru)
    else:
        dictionary = str.maketrans(ru, eng)
    return string.translate(dictionary)

print(translate(input("Введите слово: "))) 