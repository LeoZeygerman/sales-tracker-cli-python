class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_info(self):
        print(f'ID: {self.id} | Продукт: {self.name} | Цена: {self.price} | Количество: {self.quantity}')
        
    def change_price(self, new_price):
        self.price = new_price
        
    def sell_product(self, amount):
        self.quantity -= amount
        
    def add_product(self, amount):
        self.quantity += amount