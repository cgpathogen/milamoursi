from pages.main_page.main_page import MainPage
from pages.search_results_page.search_result_page import SearchResultPage
from pages.cart_page.cart_page import CartPage
from pages.order_page.order_page import OrderPage
from pages.personal_page.personal_page import PersonalCabinetPage

from data.credentials.credentials import Credentials

class BaseTest:

    def setup_method(self):
        self.mainPage = MainPage(self.driver)
        self.searchResultPage = SearchResultPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.orderPage = OrderPage(self.driver)
        self.personalPage = PersonalCabinetPage(self.driver)
        self.credentials = Credentials()