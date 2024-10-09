import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_ingredient_get_price(self):
        ingredient = Ingredient('SAUCE', 'Good sauce', 7)
        assert ingredient.get_price() == 7

    def test_ingredient_get_name(self):
        ingredient = Ingredient('SAUCE', 'Good sauce', 7)
        assert ingredient.get_name() == 'Good sauce'

    @pytest.mark.parametrize('addition, addition_type',
                             [
                                 ['SAUCE', INGREDIENT_TYPE_SAUCE],
                                 ['FILLING', INGREDIENT_TYPE_FILLING]
                             ]
                             )
    def test_ingredient_get_type_sauce(self, addition, addition_type):
        ingredient = Ingredient(addition, 'Good sauce', 7)
        assert ingredient.get_type() == addition_type
