from tests.tests_UI.base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver
