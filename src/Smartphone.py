from src.Product import Product


class Smartphone(Product):
    """ Класс для определения продукта типа смартфон"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Конструктор для определения смартфона"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        """Метод для сложения стоимости товаров вида смартфон"""

        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError
