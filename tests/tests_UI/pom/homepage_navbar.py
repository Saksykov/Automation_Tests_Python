from tests.tests_UI.base.seleniumbase import SeleniumBase


class HomepageNavbar(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver
        """
        navbar objects
        """
        self.navbar_brand = self.is_present(find_by='css_selector', locator='a.navbar-brand')
        self.navbar_logo = self.is_visible(find_by='css_selector', locator='a.navbar-brand img')
        self.nav_dropdown_items = self.are_present(find_by='css_selector', locator='ul.navbar-nav.ml-auto>li')
