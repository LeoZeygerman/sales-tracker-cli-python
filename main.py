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
        
        if choice == 1:
            name = input('Введите название товара: ')
            price = int(input('Введите цену товара: '))
            quantity = int(input('Введите количество товара: '))
            data = load_data()
            if len(data) == 0:
                new_id = 1
            else:
                new_id = data[-1]['new_id'] + 1
                
            product = {
                'new_id': new_id,
                'name': name,
                'price': price,
                'quantity': quantity
            }
            data.append(product)
            save_data(data)
            product_object = Product(new_id, name, price, quantity)
            product_object.get_info()
        
    except ValueError:
        print('Ошибка при вводе.')
