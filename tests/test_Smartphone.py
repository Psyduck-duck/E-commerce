import pytest

from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


@pytest.fixture
def some_smartphone():
    return Smartphone("Iphone", "last Iphone", 100000, 10, "max", "16", "1 TB", "Black")


@pytest.fixture
def some_lawn_grass():
    return LawnGrass("Grass", "Nice Grass", 2, 150, "Russia", "2 months", "Red")


@pytest.fixture
def some_smartphone_1():
    return Smartphone("Samsung", "last model", 150000, 20, "max", "NOTEXPROGIBRIDTURBONITRO", "15 TB", "Silver")


def test_Smartphone(some_smartphone):
    assert some_smartphone.name == "Iphone"
    assert some_smartphone.model == "16"
    assert some_smartphone.color == "Black"


def test_add_smartphone(some_smartphone, some_smartphone_1, some_lawn_grass):
    assert some_smartphone + some_smartphone_1 == 4000000
    with pytest.raises(TypeError):
        some_smartphone + some_lawn_grass
