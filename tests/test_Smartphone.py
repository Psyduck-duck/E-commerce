import pytest

from src.Smartphone import Smartphone


@pytest.fixture
def some_smartphone():
    return Smartphone("Iphone", "last Iphone", 100000, 10, "max", "16", "1 TB", "Black")


def test_Smartphone(some_smartphone):
    assert some_smartphone.name == "Iphone"
    assert some_smartphone.model == "16"
    assert some_smartphone.color == "Black"