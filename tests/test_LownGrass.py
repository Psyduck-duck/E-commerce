import pytest

from src.LawnGrass import LownGrass


@pytest.fixture
def some_lown_grass():
    return LownGrass("Grass", "Nice Grass", 2, 150, "Russia", "2 months", "Red")


def test_lown_grass(some_lown_grass):
    assert some_lown_grass.name == "Grass"
    assert some_lown_grass.country == "Russia"
    assert some_lown_grass.color == "Red"
