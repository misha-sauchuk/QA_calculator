from selenium import webdriver
from fixture.numbers import NumberHelper
from fixture.symbols import SymbolHelper


class Application:

    def __init__(self):
        # self.wd = webdriver.Firefox()
        self.wd = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.wd.implicitly_wait(5)
        self.number = NumberHelper(self)
        self.symbol = SymbolHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://qa-test.klika-tech.com/")

    def destroy(self):
        self.wd.quit()
