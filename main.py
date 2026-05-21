from storage import save_data, load_data
from models import Product
while True:
    try:
        print('1.Добавить продукт')
        print('2.Список товаров')
        print('3.Продать товар')
        print('4.Найти товар')
        print('5.Удалить товар')
        print('6.Выйти')
        choice = int(input('Введите номер интересующей вас операции: '))
    except ValueError:
        print('Ошибка при вводе.')
