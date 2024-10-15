from src.Category import Category
from src.Product import Product


class CategoryIterator:
    """Класс для итерации продуктов из объектов класса Category"""

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0


    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        self.products_list = self.category.products.rstrip().split("\n")
        if self.index < len(self.products_list):
            product = self.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
