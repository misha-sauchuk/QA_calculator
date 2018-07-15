# -*- coding: utf-8 -*-
from model.number_int import NumberInt
import pytest


test_data = range(0, 10)


@pytest.mark.parametrize("digit", test_data)
def test_display_digit(app, digit):
    app.open_home_page()
    app.number.add_one_digit(NumberInt(digit))
    result = app.number.display_text()
    assert result == str(digit)



