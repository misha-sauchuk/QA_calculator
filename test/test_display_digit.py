# -*- coding: utf-8 -*-
from model.number_int import NumberInt
import pytest

#
# def is_alert_present(wd):
#     try:
#         wd.switch_to_alert().text
#         return True
#     except:
#         return False
test_data = range(0, 10)

@pytest.mark.parametrize("digit", test_data)
def test_display_digit(app, digit):
    app.open_home_page()
    app.number.add_one_digit(NumberInt(digit))
    result = app.number.display_text()
    assert result == str(digit)



#
# class TestDivisionByZero(unittest.TestCase):
#     def setUp(self):
#         self.app = Application()

    # def test_division_by_zero(self):
    #     wd = self.wd
    #     # open home page
    #     wd.get("http://qa-test.klika-tech.com/")
    #     # make operation
    #     self.add_operand(wd)
    #     wd.find_element_by_xpath("//ul[@class='operations']//li[.='/']").click()
    #     #self.add_operand(wd)
    #     wd.find_element_by_xpath("//ul[@class='digits']//li[.='0']").click()
    #     # wd.find_element_by_css_selector("li.double").click()
    #     wd.find_element_by_xpath("//ul[@class='operations']//li[.='=']").click()
    #     for element in wd.find_elements_by_css_selector("div.display"):
    #         text = element.text
    #         assert text == 'Infinity'
    #     wd.find_element_by_xpath("//ul[@class='operations']//li[.='AC']").click()

    # def test_max_input(self):
    #     wd = self.wd
    #     wd.get("http://qa-test.klika-tech.com/")
    #     for digit in range(1,9):
    #         for i in range(0,20):
    #             self.add_one_digit(wd,digit)
    #         for element in wd.find_elements_by_css_selector("div.display"):
    #             text = element.text
    #             assert text == str(digit)*20
    #         wd.find_element_by_xpath("//ul[@class='operations']//li[.='AC']").click()

    # testdata = [
    #     1,2,3
    # ]
    # @pytest.mark.parametrize("digit", testdata)
    #
    # def tearDown(self):
    #     self.app.destroy()


# if __name__ == '__main__':
#     unittest.main()
