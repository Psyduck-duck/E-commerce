import pytest

from src.Category import Category

@pytest.fixture
def some_category():
    return Category("Болты", "Нестандартка", ["Болт М8 60", "Болт М10 100", "Болт М12 40"])


def test_Category(some_category):
    x = some_category
    y = Category("Болты", "Нестандартка", ["Болт М8 60", "Болт М10 100"])
    assert x.name == "Болты"
    assert x.description == "Нестандартка"
    assert x.products == ["Болт М8 60", "Болт М10 100", "Болт М12 40"]
    assert Category.count_products == 5
    assert Category.count_categories == 2
