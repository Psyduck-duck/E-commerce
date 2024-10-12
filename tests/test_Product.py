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


def test_new_product():
    params_dict = {"name": "name", "description": "description", "price": 1, "quantity": 2}
    product = Product.new_product(params_dict)
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 1
    assert product.quantity == 2


def test_new_price(some_product):
    assert some_product.price == 2.5
    some_product.price = 2
    assert some_product.price == 2
