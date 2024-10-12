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
            if new_price < self.__price:
                var = input("Вы действительно хотите понизить цену?: ")
                if var == "y":
                    self.__price = new_price
                else:
                    print("Отмена операции")
            else:
                self.__price = new_price
        else:
            print("“Цена не должна быть нулевая или отрицательная”")


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
