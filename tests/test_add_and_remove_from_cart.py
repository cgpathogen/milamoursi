import time

from base.base_test import BaseTest


class TestAddToCart(BaseTest):

    def test_open(self):
        self.mainPage.open()
        self.mainPage.click_accept_cookie()
        self.mainPage.click_search_input_button()
        self.mainPage.enter_text("крем")
        self.searchResultPage.scroll(0, 300)
        self.searchResultPage.add_several_items()
        # self.searchResultPage.hover_item()
        # self.searchResultPage.click_add_to_cart_button()
        # self.searchResultPage.get_off_canvas_block()
        self.searchResultPage.click_cart_button()
        time.sleep(3)