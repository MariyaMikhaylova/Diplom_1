from praktikum.bun import Bun


class TestBun:

    def test_bun_get_name(self):
        bun = Bun("Goog bon", 17)
        assert bun.get_name() == "Goog bon"

    def test_bun_get_price(self):
        bun = Bun("Goog bon", 17)
        assert bun.get_price() == 17

    def test_bun_get_name_price(self):
        bun = Bun("Goog bon", 17)
        assert (bun.get_name() == "Goog bon"
                and bun.get_price() == 17)
