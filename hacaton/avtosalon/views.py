from .models import Cars
from pprint import pprint
def cars_create():
    mark = input('Введите название марки: ')
    model = input('Введите название модели: ')
    year = int(input('Введите год выпуска: '))
    volume = float(input('Введите объем двигателя: '))
    color = input('Выберите цвет: ')
    type_ = input(f'Выберите тип кузова из предложенных вариантов:\n{Cars.type_kuz}: ')
    prob = input('Введите пробег: ')
    price = float(input('Введите цену: '))
    Cars(mark, model, year, volume, color, type_, prob, price)
    print('Машина добавлена!')

def cars_listing():
    fields = ['Марка', 'Модель', 'Год выпуска', 'Цвет', 'Типа кузова', 'Пробег', 'Цена']
    list_ = []
    for car in Cars.objects:
        list_.append({'Марка':car.mark, 'Модель':car.model, 'Год выпуска':car.year, 'Оъем':car.volume, 'Цвет':car.color, 'Тип кузова':car.type_, 'Пробег':car.prob, 'Цена':car.price})
    pprint(list_)

def cars_retrieve(_id):
    list_ = []
    for car in Cars.objects:
        list_.append({'Марка':car.mark, 'Модель':car.model, 'Год выпуска':car.year, 'Объем':car.volume, 'Цвет':car.color, 'Тип кузова':car.type_, 'Пробег':car.prob, 'Цена':car.price})
    print(list_[_id])

def cars_update(_id):
    car = Cars.objects[_id]
    field = input("Введите поле для изменения(mark, model, year, volume, color, type_, prob, price): ")
    if field in dir(car):
        print(f"old value: {getattr(car, field)}")
        value = input(f"{field} = ")
        if field == 'type_':
            if value not in Cars.type_kuz:
                raise Exception(f'Введите верный тип! {Cars.type_kuz}')
        setattr(car, field, value)
    else:
        raise Exception(f"Поля {field} не cуществует!")
    cars_listing()


def cars_delete(_id):
    car = Cars.objects[_id]
    Cars.objects.remove(car)
    print('Машина удалена!')
    cars_listing()