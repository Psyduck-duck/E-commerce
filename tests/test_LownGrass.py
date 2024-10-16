import pytest

from src.LawnGrass import LawnGrass
from src.Smartphone import Smartphone


@pytest.fixture
def some_lawn_grass():
    return LawnGrass("Grass", "Nice Grass", 2, 150, "Russia", "2 months", "Red")


@pytest.fixture
def some_lawn_grass_1():
    return LawnGrass("Grass", "Bad Grass", 1, 300, "USA", "4 months", "Yellow")


@pytest.fixture
def some_smartphone():
    return Smartphone("Iphone", "last Iphone", 100000, 10, "max", "16", "1 TB", "Black")


def test_lown_grass(some_lawn_grass):
    assert some_lawn_grass.name == "Grass"
    assert some_lawn_grass.country == "Russia"
    assert some_lawn_grass.color == "Red"


def test_add_lawn_grass(some_lawn_grass, some_lawn_grass_1, some_smartphone):
    assert some_lawn_grass + some_lawn_grass_1 == 600
    with pytest.raises(TypeError):
        some_lawn_grass + some_smartphone
