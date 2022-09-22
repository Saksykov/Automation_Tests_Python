from tests.tests_UI.pom.homepage_navbar import HomepageNavbar


def test_navbar_brand(chr_driver):
    navbar = HomepageNavbar(chr_driver)
    brand = navbar.navbar_brand
    brand.click()
