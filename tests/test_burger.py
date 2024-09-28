from praktikum.burger import Burger


class TestBurger:

    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert (burger.bun.get_name() == "Good bun"
                and burger.bun.get_price() == 17)

    def test_burger_add_sauce(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert (burger.ingredients[0].get_price() == 7
                and burger.ingredients[0].get_name() == "Good sauce"
                and burger.ingredients[0].get_type() == 'SAUCE')

    def test_burger_add_filling(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        assert (burger.ingredients[0].get_price() == 27
                and burger.ingredients[0].get_name() == "Good filling"
                and burger.ingredients[0].get_type() == 'FILLING')

    def test_burger_add_bun_and_all_ingredients(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert (burger.bun.get_name() == "Good bun"
                and burger.bun.get_price() == 17
                and burger.ingredients[0].get_price() == 7
                and burger.ingredients[0].get_name() == "Good sauce"
                and burger.ingredients[0].get_type() == 'SAUCE'
                and burger.ingredients[1].get_price() == 27
                and burger.ingredients[1].get_name() == "Good filling"
                and burger.ingredients[1].get_type() == 'FILLING')

    def test_burger_remove_ingredient(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_burger_get_price(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.get_price() == 68

    def test_burger_get_receipt(self, mock_bun, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.get_receipt() == ('(==== Good bun ====)\n'
                                        '= filling Good filling =\n'
                                        '(==== Good bun ====)\n\n'
                                        'Price: 61')
