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
            
        if choice == 2:
            data = load_data()
            for user in data:
                print(f'ID: {user['new_id']} | Товар: {user['name']} | Цена: {user['price']} | Количество: {user['quantity']}')
                
        if choice == 3:
            which_product = input('Введите название или ID продукта, который хотите продать: ')
            data = load_data()
            found = False
            for user in data: 
                if(
                    str(user['new_id']) == which_product
                    or user['name'] == which_product
                    and int(user['quantity']) > 0
                ):
                    found = True
                    product_object = Product(user['new_id'], user['name'], user['price'], user['quantity'])
                    amount = int(input(f'Введите количество продукта {user['name']}, которое хотите продать: '))
                    product_object.sell_product(amount)
                    user['quantity'] = product_object.quantity
                    print(f'Остаток продукта {user['name']}: {user['quantity']}')
            save_data(data)
            if not found:
                print(f'Ошибка в поиске товара.')
                
        if choice == 4:
            search = input('Введите название или ID товара, который вы хотите найти: ')
            data = load_data()
            found = False
            for user in data: 
                if(
                    str(user['new_id']) == search
                    or user['name'] == search
                ):
                    found = True
                    product_object = Product(user['new_id'], user['name'], user['price'], user['quantity'])
                    product_object.get_info()
            save_data(data)
            if not found:
                print(f'Ошибка в поиске товара.')
        
    except ValueError:
        print('Ошибка при вводе.')
