import pytest
from tests.tests_UI.pom.homepage_navbar import HomepageNavbar


class TestNavbar:
    """
    In class we testing Home Page Navbar objects
    """
    @pytest.mark.parametrize()
    def test_navbar(self, chr_driver):
        navbar = HomepageNavbar(chr_driver)
        brand = navbar.navbar_brand
        print(brand)
