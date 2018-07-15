from selenium import webdriver
from fixture.numbers import NumberHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.wd.implicitly_wait(5)
        self.number = NumberHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://qa-test.klika-tech.com/")

    def destroy(self):
        self.wd.quit()
