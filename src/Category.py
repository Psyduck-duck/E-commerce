import json


class Category:
    """ Класс для обозначения группы продуктов"""

    name: str
    description: str
    products: list
    count_categories = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_categories += 1
        Category.count_products += len(products)


def read_json_file(filename:str) -> list:
    pass
