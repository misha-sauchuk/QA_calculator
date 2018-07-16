# -*- coding: utf-8 -*-
from model.symbol import MathSymbol
import pytest


test_data = [
    '+', '-', '/','x', '=',
]


@pytest.mark.parametrize("symbol", test_data)
def test_display_symbol(app, symbol):
    app.open_home_page()
    app.symbol.add_one_symbol(MathSymbol(symbol))
    result = app.symbol.display_text()
    if symbol == '=':
        assert result == '0'
    else:
        assert result == symbol
