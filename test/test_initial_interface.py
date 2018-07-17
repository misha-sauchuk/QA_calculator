# -*- coding: utf-8 -*-
from model.symbol import MathSymbol


def test_initial_interface(app):
    app.open_home_page()
    result = app.symbol.display_text()
    assert result == '0'
