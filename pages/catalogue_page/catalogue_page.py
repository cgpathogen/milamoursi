from pages.base_page.base_page import BasePage
from pages.catalogue_page.components.filters import Filters



class CataloguePage(BasePage):

    page_url = "https://milamoursi.ru/catalog"

    def __init__(self, driver):
        super().__init__(driver)
        self.filters = Filters(driver)