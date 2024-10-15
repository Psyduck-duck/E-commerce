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

    def __str__(self):
        self.products_quantity = 0
        for product in self.__products:
            self.products_quantity += product.quantity

        return f"{self.name}, количество продуктов: {self.products_quantity}"

    def add_product(self, name, description, price, quantity):
        """Добавляет продукт в список продуктов"""

        self.__products.append(Product(name, description, price, quantity))
        Category.count_products += 1

    @property
    def products(self):
        """Возвращает информацию о продуктах в виде строки"""
        product_list = []
        for product in self.__products:
            product_list.append(f"{str(product)}\n")

        product_str = "".join(product_list)
        return product_str
