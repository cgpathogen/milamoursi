import time
from base.base_test import BaseTest

class TestCart(BaseTest):

    def test_add_remove_several_products(self):
        self.mainPage.open()
        self.mainPage.click_accept_cookie()
        self.mainPage.click_search_input_button()
        self.mainPage.enter_text("крем")
        self.searchResultPage.scroll(0, 300)
        self.searchResultPage.add_several_items()
        self.searchResultPage.click_cart_button()
        self.cartPage.remove_from_cart_()