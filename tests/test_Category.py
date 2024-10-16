import pytest

from src.Category import Category
from src.LawnGrass import LawnGrass
from src.iteration_category import CategoryIterator
from src.Product import Product


@pytest.fixture
def some_category():
    product_1 = Product("Болт М8 60", "Болт М8 60 ГОСТ 20236511", 2.5, 150)
    product_2 = Product("Болт М10 100", "Болт М10 100 ГОСТ 20236511", 4.5, 100)
    product_3 = Product("Болт М12 40", "Болт М12 40 ГОСТ 20236511", 3, 50)
    return Category("Болты", "Нестандартка", [product_1, product_2, product_3])


@pytest.fixture
def some_product():
    return Product("Болт М24 170", "Болт М24 170 ГОСТ 6552714", 2.50, 1200)


@pytest.fixture
def some_lawn_grass():
    return LawnGrass("Grass", "Nice Grass", 2, 150, "Russia", "2 months", "Red")


def test_Category(some_category):
    x = some_category
    y = Category("Болты", "Нестандартка", ["Болт М8 60", "Болт М10 100"])
    assert x.name == "Болты"
    assert x.description == "Нестандартка"
    assert (
        x.products
        == "Болт М8 60, 2.5 руб. Остаток: 150 шт.\nБолт М10 100, 4.5 руб. Остаток: 100 шт.\nБолт М12 40, 3 руб. Остаток: 50 шт.\n"
    )
    assert Category.count_products == 5
    assert Category.count_categories == 2


class LeftClass:
    pass


def test_add_product(some_category, some_product, some_lawn_grass):
    assert len((some_category.products.rstrip()).split("\n")) == 3
    some_category.add_product(some_product)
    assert len((some_category.products.rstrip()).split("\n")) == 4
    some_category.add_product(some_lawn_grass)
    assert len((some_category.products.rstrip()).split("\n")) == 5
    with pytest.raises(TypeError):
        some_category.add_product(LeftClass())


def test_str_category(some_category):
    assert str(some_category) == "Болты, количество продуктов: 300"


def test_category_iteration(some_category):
    iterator = CategoryIterator(some_category)
    assert iterator.index == 0
    assert next(iterator) == "Болт М8 60, 2.5 руб. Остаток: 150 шт."
    assert next(iterator) == "Болт М10 100, 4.5 руб. Остаток: 100 шт."
    assert next(iterator) == "Болт М12 40, 3 руб. Остаток: 50 шт."

    with pytest.raises(StopIteration):
        next(iterator)
