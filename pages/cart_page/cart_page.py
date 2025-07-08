from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from count import count

class CartPage(BasePage):

    page_url = "https://milamoursi.ru/personal/cart/"

    # locators

    item_name_locator = "(//a[@class='font-weight-500 mb-1 text-secondary'])"
    one_item_price = "(//p[@class='card-text font-weight-bold fs-14 mb-1 text-secondary'])"
    final_item_price = "(//p[@class='mb-0 text-secondary font-weight-bold mr-xl-11'])"
    total_price_locator = "(//*[@id='basket_form']/div[2]/div[3]/div/div[2]/div/span[2])"
    cross_button_locator = "(//a[@class='d-block'])"
    empty = "//p[@class='fs-18 lh-155 mx-auto']"

    # getters

    def get_total_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.total_price_locator))).text

    def get_empty(self):
        return self.wait.until(EC.presence_of_element_located(self.locator_maker(self.empty)))

    # actions

    def wait_for_message(self):
        assert self.get_empty().text == "Ваша корзина пуста"

    # methods

    def remove_from_cart_(self):
        for i in range(1, count):
            # внутренний геттер для перебора кнопок по индексу
            getter_cross_button = self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.cross_button_locator,i)))
            getter_cross_button.click()
        self.wait_for_message() # завершение теста через ожидание сообщения "Корзина пуста"