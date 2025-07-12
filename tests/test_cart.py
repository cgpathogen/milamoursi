import allure
from base.base_test import BaseTest

@allure.epic("Products")
@allure.story("Cart")
class TestCart(BaseTest):

    @allure.title("Add items to cart/Remove items from cart")
    @allure.feature("Basic cart operation")
    def test_add_remove_several_products(self):
        self.mainPage.open()
        self.mainPage.click_accept_cookie()
        self.mainPage.click_search_input_button()
        self.mainPage.enter_text("крем")
        self.searchResultPage.scroll(0, 400)
        self.searchResultPage.add_several_items()
        self.searchResultPage.click_cart_button()
        self.cartPage.remove_from_cart_()