import pytest

from unittest.mock import patch

from src.Product import Product



@pytest.fixture
def some_product():
    return Product("Болт М24 170", "Болт М24 170 ГОСТ 6552714", 2.50, 1200)


def test_Product(some_product):
    x = some_product
    assert x.name == "Болт М24 170"
    assert x.description == "Болт М24 170 ГОСТ 6552714"
    assert x.price == 2.50
    assert x.quantity == 1200


def test_new_product():
    params_dict = {"name": "name", "description": "description", "price": 1, "quantity": 2}
    product = Product.new_product(params_dict)
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 1
    assert product.quantity == 2


def test_dubl_product(some_product):

    params = {"name": "Болт М24 170", "description": "Болт М24 170 ГОСТ 6552714", "price": 3.50, "quantity": 200}
    assert some_product.name == "Болт М24 170"
    assert some_product.description == "Болт М24 170 ГОСТ 6552714"
    assert some_product.price == 2.50
    assert some_product.quantity == 1200
    new_product = Product.new_product(params, [some_product])
    assert some_product.name == "Болт М24 170"
    assert some_product.description == "Болт М24 170 ГОСТ 6552714"
    assert some_product.price == 3.50
    assert some_product.quantity == 1400



def test_new_price(some_product):
    assert some_product.price == 2.5
    some_product.price = 3
    assert some_product.price == 3


@patch("src.Product.input")
def test_new_low_price(mock_input, some_product):
    mock_input.return_value = "y"
    assert some_product.price == 2.5
    some_product.price = 2
    assert some_product.price == 2
