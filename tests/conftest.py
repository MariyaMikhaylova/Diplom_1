from unittest.mock import Mock

import pytest

from praktikum import ingredient_types
from praktikum.database import Database


@pytest.fixture(scope="function")
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Good bun"
    bun.get_price.return_value = 17

    return bun


@pytest.fixture(scope="function")
def mock_ingredient_sauce():
    ingredient_sauce = Mock()
    ingredient_sauce.get_price.return_value = 7
    ingredient_sauce.get_name.return_value = "Good sauce"
    ingredient_sauce.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE

    return ingredient_sauce


@pytest.fixture(scope="function")
def mock_ingredient_filling():
    ingredient_filling = Mock()
    ingredient_filling.get_price.return_value = 27
    ingredient_filling.get_name.return_value = "Good filling"
    ingredient_filling.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING

    return ingredient_filling


@pytest.fixture(scope="function")
def database():
    database = Database()
    return database
