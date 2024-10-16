from src.Product import Product


class LawnGrass(Product):
    """Класс для определения продукта (газонная трава)"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Конструктор для определения травы газонной"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод для сложения стоимости товаров вида трава газонная"""

        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError
