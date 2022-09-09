import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def get_chr_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1280,960')
    return options


@pytest.fixture()
def get_chr_driver(get_chr_options):
    executable_path = r'C:\WebDrivers\chromedriver\chromedriver.exe'
    options = get_chr_options
    driver = webdriver.Chrome(executable_path=executable_path, options=options)
    return driver


@pytest.fixture(scope='function')
def startup(request, get_chr_driver):
    driver = get_chr_driver
    url = 'https://timetta.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url=url)
    yield driver
    driver.quit()
