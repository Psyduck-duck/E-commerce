import json
import os

from data.path_to_directory import PATH_TO_DATA_DIRECTORY
from src.Product import Product


class Category:
    """Класс для обозначения группы продуктов"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        self.products_quantity = 0
        for product in self.__products:
            self.products_quantity += product.quantity

        return f"{self.name}, количество продуктов: {self.products_quantity}"

    def add_product(self, some_product):
        """Добавляет продукт в список продуктов"""
        if isinstance(some_product, Product):
            self.__products.append(some_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Возвращает информацию о продуктах в виде строки"""
        product_list = []
        for product in self.__products:
            product_list.append(f"{str(product)}\n")

        product_str = "".join(product_list)
        return product_str

    @property
    def avg_price(self):
        try:
            self.__products[0]
        except IndexError:
            return 0
        except Exception:
            print("something wrong")

        total_price_for_products_list = []   #Лист для сбора общей стоимости каждого продукта
        total_count_products = 0
        for product in self.__products:
            total_price_for_products_list.append(product.price * product.quantity)
            total_count_products += product.quantity

        return sum(total_price_for_products_list) / total_count_products


