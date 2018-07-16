# -*- coding: utf-8 -*-
from model.number_int import NumberInt
import pytest


test_data = list(range(0, 10)) + ['.']
print(test_data)

@pytest.mark.parametrize("digit", test_data)
def test_display_digit(app, digit):
    app.open_home_page()
    app.number.add_one_digit(NumberInt(digit))
    result = app.number.display_text()
    if digit == '.':
        assert result == '0.'
    else:
        assert result == str(digit)
