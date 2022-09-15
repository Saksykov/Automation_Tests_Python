import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeDriver:

    def __init__(self, options_list: list, executable_path):
        self.options = Options()
        self.options_list = options_list
        for option in self.options_list:
            self.options.add_argument(option)
        self.executable_path = executable_path
        self.driver = webdriver.Chrome(executable_path=self.executable_path, options=self.options)

    def get_driver(self):
        return self.driver


@pytest.fixture(scope='function')
def chr_driver(request):
    chrome_driver = ChromeDriver(options_list=['chrome', '--start-maximized', '--window-size=1280,960'],
                                 executable_path=r'C:\WebDrivers\chromedriver\chromedriver.exe')
    driver = chrome_driver.get_driver()
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url='https://timetta.com/')
    yield driver
    driver.quit()
