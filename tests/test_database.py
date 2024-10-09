import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize('name, price',
                             [
                                 ["black bun", 100],
                                 ["white bun", 200],
                                 ["red bun", 300]
                             ]
                             )
    def test_available_buns_in_database(self, name, price, database):
        bun_exist = False
        for bun in database.available_buns():
            if bun.get_name() == name and bun.get_price() == price:
                bun_exist = True
                break
        assert bun_exist

    @pytest.mark.parametrize('type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                                 [INGREDIENT_TYPE_SAUCE, "sour cream", 200],
                                 [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
                                 [INGREDIENT_TYPE_FILLING, "cutlet", 100],
                                 [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
                                 [INGREDIENT_TYPE_FILLING, "sausage", 300]
                             ]
                             )
    def test_available_ingredients(self, type, name, price, database):
        ingredients_exist = False
        for ingredient in database.available_ingredients():
            if (ingredient.get_type() == type
                    and ingredient.get_name() == name
                    and ingredient.get_price() == price):
                ingredients_exist = True
                break
        assert ingredients_exist
