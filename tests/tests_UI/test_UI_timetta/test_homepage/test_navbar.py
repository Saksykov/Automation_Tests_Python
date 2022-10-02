import pytest
from tests.tests_UI.pom.homepage_navbar import HomepageNavbar


@pytest.fixture(autouse='False')
def navbar(chr_driver):
    navbar = HomepageNavbar(chr_driver)
    return navbar


def test_navbar_brand(chr_driver, navbar):
    brand = navbar.navbar_brand
    brand.click()
    assert chr_driver.current_url == 'https://timetta.com/'


def test_navbar_logo(navbar):
    logo = navbar.navbar_logo
    assert '/images/timetta-logo.svg' in logo.get_attribute('src')


def test_nav_dropdown_items(navbar):
    dropdown_items = navbar.nav_dropdown_items
    items = navbar.get_text_from_webelements(dropdown_items)
    assert items == ['Features', 'Industries', 'Pricing', 'Resources']


def test_language_switch(navbar, chr_driver):
    lang_switch = navbar.language_switch
    assert lang_switch.text.lower() == 'ru'
    lang_switch.click()
    assert chr_driver.current_url == 'https://timetta.com/ru'


def test_sign_in(navbar, chr_driver):
    sign_in = navbar.sign_in
    assert sign_in.text.lower() == 'sign in'
    sign_in.click()
    assert 'https://auth.timetta.com/' in chr_driver.current_url
