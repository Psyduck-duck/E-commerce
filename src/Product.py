class Product:
    """ Класс для определения продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, params_dict):
        name = params_dict.get("name")
        description = params_dict.get("description")
        price = params_dict.get("price")
        quantity = params_dict.get("quantity")
        return cls(name, description, price, quantity)
