from unittest.mock import patch

import pytest

from src.LawnGrass import LawnGrass
from src.Product import Product


@pytest.fixture
def some_product():
    return Product("Болт М24 170", "Болт М24 170 ГОСТ 6552714", 2.50, 1200)


@pytest.fixture
def some_product_2():
    return Product("Болт М10 100", "Болт М10 100 ГОСТ 20236511", 4.5, 1000)


def test_Product(some_product, capsys):
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


def test_dubl_product(some_product, capsys):

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
    message = capsys.readouterr()
    assert message.out.strip() == "Продукт успешо добавлен к существующему."


def test_new_price(some_product):
    assert some_product.price == 2.5
    some_product.price = 3
    assert some_product.price == 3


def test_new_low_price(capsys, some_product):
    assert some_product.price == 2.5
    some_product.price = -1
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


@patch("src.Product.input")
def test_new_low_price(mock_input, some_product):
    mock_input.return_value = "y"
    assert some_product.price == 2.5
    some_product.price = 2
    assert some_product.price == 2


@patch("src.Product.input")
def test_new_low_price_no_verification(mock_input, capsys, some_product):
    mock_input.return_value = "n"
    assert some_product.price == 2.5
    some_product.price = 2
    message = capsys.readouterr()
    assert message.out.strip() == "Product ('Болт М24 170', 'Болт М24 170 ГОСТ 6552714', 2.5, 1200)\nОтмена операции"


def test_str_product(some_product):
    assert str(some_product) == "Болт М24 170, 2.5 руб. Остаток: 1200 шт."


def test_add_products(some_product, some_product_2):
    assert some_product + some_product_2 == 7500


def test_MixinPrintInfo(capsys):
    product = LawnGrass("grass", "lawn grass", 12, 100, "Russia", "3 month", "green")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass ('grass', 'lawn grass', 12, 100)"
