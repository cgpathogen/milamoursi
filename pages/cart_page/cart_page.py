from database.database import Database
from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from count import count

class CartPage(BasePage):

    page_url = "https://milamoursi.ru/personal/cart/"

    # locators

    item_name_locator = "(//a[@class='font-weight-500 mb-1 text-secondary'])" # название товара
    one_item_price = "(//p[@class='card-text font-weight-bold fs-14 mb-1 text-secondary'])" # актуальная, незачёркнутая цена
    final_item_price = "(//p[@class='mb-0 text-secondary font-weight-bold mr-xl-11'])" # цена в блоке справа
    total_price_locator = "(//*[@id='basket_form']/div[2]/div[3]/div/div[2]/div/span[2])"  # суммарная цена за заказ
    cross_button_locator = "(//a[@class='d-block'])" # кнопка-крести удаления из корзины
    empty = "//p[@class='fs-18 lh-155 mx-auto']" # сообщение "Корзина пуста"
    item_counter_locator = "//*[@id='basket_form']/div[1]/table/tbody/tr" # счётчик единиц товара, общий локатор
    go_to_cart_locator = "//*[@id='basket_form']/div[2]/div[3]/div/div[2]/button"

    # getters

    def get_total_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.total_price_locator)))

    def get_empty(self):
        return self.wait.until(EC.presence_of_element_located(self.locator_maker(self.empty)))

    def get_go_to_cart(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.go_to_cart_locator)))

    # actions

    @allure.step("Waiting for message the cart is empty")
    def wait_for_message(self):
        assert self.get_empty().text == "Ваша корзина пуста"

    @allure.step("Click go to cart button on cart page")
    def click_go_to_cart_button(self):
        self.get_go_to_cart().click()

    # methods

    @allure.step("Removal items from cart")
    def remove_from_cart_(self):
        for i in range(1, count):
            # внутренний геттер для перебора кнопок по индексу
            getter_cross_button = self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.cross_button_locator,i)))
            getter_cross_button.click()
        self.wait_for_message() # завершение теста через ожидание сообщения "Корзина пуста"


    @allure.step("Compare names and prices")
    def compare_names_and_prices(self):
        sum = 0
        total_price = self.divide_price(self.get_total_price().text)
        for i in range(1, count):
            # locators
            item_name_getter = self.wait.until(EC.visibility_of_element_located(
                self.locator_maker(self.item_name_locator,i)))
            one_item_price_getter = self.wait.until(EC.visibility_of_element_located(
                self.locator_maker(self.one_item_price,i,"/span[2]")))
            final_item_price_getter = self.wait.until(EC.visibility_of_element_located(
                self.locator_maker(self.final_item_price,i)))
            # get prices
            one_price = self.divide_price(one_item_price_getter.text,True)
            final_price = self.divide_price(final_item_price_getter.text)
            #asertions
            assert item_name_getter.text == Database.select_item_data(i)[0]
            assert one_price == Database.select_item_data(i)[1]
            assert one_price == final_price
            sum += final_price
        assert sum == total_price