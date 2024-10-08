import pytest

from src.Product import Product

@pytest.fixture
def some_product():
    return Product("болт", "болт М24 170", 2.50, 1200)


def test_Product(some_product):
    x = some_product
    assert x.name == "болт"
    assert x.description == "болт М24 170"
    assert x.price == 2.50
    assert x.quantity == 1200
