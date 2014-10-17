class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.storage = {}
        self.income = 0

    def load_new_products(self, product, count):
        if product in self.storage:
            self.storage[product] += count
        else:
            self.storage[product] = count

    def list_products(self, product_class):
        for key, value in self.storage.items():
            if isinstance(key, product_class):
                print('{} : {}'.format(key.name, value))

    def sell_product(self, product):
        if product in self.storage and self.storage[product] > 0:
            self.storage[product] -= 1
            self.income += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.income

laptop = Laptop("Hackbook", 1000, 1300, 1000, 8)
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store = Store('Laptop.bg')
store.load_new_products(smarthphone, 2)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone)

print (store.total_income()) # 640