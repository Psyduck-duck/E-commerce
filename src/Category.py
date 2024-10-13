import json
import os

from data.path_to_directory import PATH_TO_DATA_DIRECTORY
from src.Product import Product


class Category:
    """Класс для обозначения группы продуктов"""

    name: str
    description: str
    __products: list
    count_categories = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.count_categories += 1
        Category.count_products += len(products)

    def add_product(self, name, description, price, quantity):
        """Добавляет продукт в список продуктов"""

        self.__products.append(Product(name, description, price, quantity))

    @property
    def products(self):
        """Возвращает информацию о продуктах в виде строки"""
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")

        product_str = "".join(product_list)
        return product_str
