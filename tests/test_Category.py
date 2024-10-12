import pytest

from src.Category import Category, read_json_file


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


def test_Category_with_json_file():
    data = read_json_file("products.json")
    categorys = []
    for i in data:
        categorys.append(Category(i.get("name"), i.get("description"), i.get("products")))

    assert categorys[0].name == "Смартфоны"
    assert categorys[1].name == "Телевизоры"
    assert (
        categorys[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert (
        categorys[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert categorys[0].products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ]
