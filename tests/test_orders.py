import allure
from base.base_test import BaseTest


@allure.epic("Products")
@allure.story("Orders")
class TestOrders(BaseTest):

    @allure.title("Place order")
    @allure.feature("...")
    def test_place_order(self):
        self.mainPage.open()
        self.mainPage.click_accept_cookie()
        self.mainPage.click_search_input_button()
        self.mainPage.enter_text("крем")
        self.searchResultPage.scroll(0, 300)
        self.searchResultPage.add_several_items()
        self.searchResultPage.click_cart_button()
        self.cartPage.compare_names_and_prices()