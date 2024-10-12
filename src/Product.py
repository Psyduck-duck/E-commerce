class Product:
    """ Класс для определения продукта"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        """геттер для цены"""

        return self.__price


    @price.setter
    def price(self, new_price):
        """сеттер для цены"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("“Цена не должна быть нулевая или отрицательная”")


    @classmethod
    def new_product(cls, params_dict):
        name = params_dict.get("name")
        description = params_dict.get("description")
        price = params_dict.get("price")
        quantity = params_dict.get("quantity")
        return cls(name, description, price, quantity)
