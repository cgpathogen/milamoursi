import time

from base. base_test import BaseTest


class TestAddToCart(BaseTest):

    def test_open(self):
        self.mainPage.open()
        self.mainPage.click_search_input_button()
        time.sleep(3)