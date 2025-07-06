from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class SearchResultPage(BasePage):

    page_url = "https://milamoursi.ru/search/"

    # locators

    item_locator = "//div[@class='col-xl-3 col-lg-4 col-6']"
    add_to_cart_button_locator = "//a[@class='btn btn-secondary lh-12']"

    # getters

    def get_item(self):
        """
        геттер для поиска первого в списке продукта
        для кейсов с покупкой нескольких товаров локаторы будут перебираться через цикл
        """
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.item_locator,1)))

    def get_add_to_cart_button(self):
        """
        геттер для клика по кнопке первого элемента
        для кейсов с покупкой нескольких товаров локаторы будут перебираться через цикл
        """
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.add_to_cart_button_locator,1)))

    # actions

    def hover_item(self):
        self.action.move_to_element(self.get_item()).perform()

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()