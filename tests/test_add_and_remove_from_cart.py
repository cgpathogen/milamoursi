import time

from base. base_test import BaseTest


class TestAddToCart(BaseTest):

    def test_open(self):
        self.mainPage.open()
        time.sleep(3)