from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для определения базовых методов для класс Product и дочерних"""

    @abstractmethod
    def __init__(self, name, description):
        """Конструктор с базовыми свойствами товара"""
        self.name = name
        self.description = description

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct):
    """Класс для определения продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description)
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """сложение стоимости всего товара"""

        return self.quantity * self.__price + other.quantity * other.__price

    @property
    def price(self):
        """геттер для цены"""

        return self.__price

    @price.setter
    def price(self, new_price):
        """сеттер для цены"""
        if new_price > 0:
            if new_price < self.__price:
                verification = input("Вы действительно хотите понизить цену?: ")
                if verification == "y":
                    self.__price = new_price
                else:
                    print("Отмена операции")
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, params_dict, check_list=None):
        """Создает новые продукт из словаря, проверяю наличие продукта в заданном списке
        с последующим прибавлением и выставление высшей цены"""

        if check_list is None:
            check_list = []
        name = params_dict.get("name")
        description = params_dict.get("description")
        price = params_dict.get("price")
        quantity = params_dict.get("quantity")

        if check_list:
            for product in check_list:
                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    print("Продукт успешо добавлен к существующему.")
                    return product

        return cls(name, description, price, quantity)
