


class NumberHelper():

    def __init__(self, app):
        self.app = app

    def add_one_digit(self, number):
        wd = self.app.wd
        path = "//ul[@class='digits']//li[.='{}']".format(number.digit)
        wd.find_element_by_xpath(path).click()

    def display_text(self):
        wd = self.app.wd
        text = wd.find_element_by_css_selector("div.display").text
        return text
