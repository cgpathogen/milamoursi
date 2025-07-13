import allure
from base.base_test import BaseTest


@allure.epic("Products")
@allure.story("Orders")
class TestOrders(BaseTest):

    @allure.title("Place order with paying in cash")
    @allure.feature("Paying")
    def test_place_order_with_paying_in_cash(self):
        self.mainPage.open()
        self.mainPage.click_accept_cookie()
        self.mainPage.click_search_input_button()
        self.mainPage.enter_text("крем")
        self.searchResultPage.scroll(0, 300)
        self.searchResultPage.add_several_items()
        self.searchResultPage.click_cart_button()
        self.cartPage.compare_names_and_prices()
        self.cartPage.click_go_to_cart_button()
        self.orderPage.choose_city()
        self.orderPage.enter_user_data()
        self.orderPage.compare_prices_and_names()


    @allure.title("Place order with paying by card via catalogue")
    @allure.feature("Paying")
    def test_order_with_paying_in_cash(self):
        self.mainPage.open()
        self.mainPage.click_accept_cookie()
        self.mainPage.hover_for_face_link()
        self.mainPage.hover_dropdown_menu()
        self.mainPage.click_day_care_link()