import json
import os

from data.path_to_directory import PATH_TO_DATA_DIRECTORY


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


def read_json_file(filename: str) -> list:
    """Функция для чтения данных из json файла"""

    path_to_file = os.path.join(PATH_TO_DATA_DIRECTORY, filename)
    with open(path_to_file, "r", encoding="utf-8") as file:
        result = json.load(file)

        return result
