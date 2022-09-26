import pytest
from tests.tests_UI.pom.homepage_navbar import HomepageNavbar


@pytest.fixture(autouse='False')
def navbar(chr_driver):
    navbar = HomepageNavbar(chr_driver)
    return navbar


def test_navbar_brand(navbar):
    brand = navbar.navbar_brand
    brand.click()


def test_nav_dropdown_items(navbar):
    dropdown_items = navbar.nav_dropdown_items
    print(dropdown_items)
