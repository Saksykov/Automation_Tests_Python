import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.ui import WebDriverWait


class TestHomePage:

    def test_home_page(self, chr_driver):
        wait = WebDriverWait(chr_driver, 15, 0.3)
        assert wait.until(exp_cond.visibility_of_element_located((By.CSS_SELECTOR, '#header img[alt="Timetta Logo"]'))).is_displayed()

