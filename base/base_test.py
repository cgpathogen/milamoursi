from pages.main_page.main_page import MainPage
from pages.search_results_page.search_result_page import SearchResultPage

class BaseTest:

    def setup_method(self):
        self.mainPage = MainPage(self.driver)
        self.searchResultPage = SearchResultPage(self.driver)