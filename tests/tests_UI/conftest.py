import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeDriver:

    def __init__(self, options_list: list):
        self.options = Options()
        self.options_list = options_list
        for option in self.options_list:
            self.options.add_argument(option)
        self.driver = webdriver.Chrome(options=self.options)

    def get_driver(self):
        return self.driver


@pytest.fixture()
def chr_driver(request):
    chrome_driver = ChromeDriver(options_list=['chrome', '--start-maximized', '--window-size=2112,1188'])  # use --headless without UI
    driver = chrome_driver.get_driver()
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url='https://timetta.com/')
    yield driver
    driver.quit()
