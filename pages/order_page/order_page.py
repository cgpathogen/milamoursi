import time

import allure
from count import count
from database.database import Database
from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementNotInteractableException

class OrderPage(BasePage):

    page_url = "https://milamoursi.ru/personal/order/make/"

    #locators

    location_name_locator = "//*[@id='order_location_name']"
    location_popup_locator = "//div[@class='popup-citySearch__cont']"
    popup_search_locator = "//input[@class='popup-search__text']"
    popup_search_result_locator = "//*[@id='ihn4_city_popup']/div[3]/div/ul[2]/li/a"
    close_popup_locator = "//*[@id='ihn4_city_popup']/div[3]/div/div[1]"

    user_name_input_locator = "//*[@id='ORDER_PROP_3']"
    phone_input_locator = "//*[@id='ORDER_PROP_4']"
    email_input_locator = "//*[@id='ORDER_PROP_5']"

    pay_in_cash_locator = "//*[@id='ID_PAY_SYSTEM_ID_2']"
    pay_by_card_locator = "//*[@id='ID_PAY_SYSTEM_ID_3']"

    item_name_locator = "(//span[@class='text-secondary pr-6'])" # /div[2]/div[1]/span
    item_price_locator = "(//p[@class='fs-14 text-secondary mb-0 font-weight-bold order-product-price'])" # /div[2]/div[2]/p
    total_price_locator = "//*[@id='order_form_content']/div[1]/div/div[3]/div/span[2]"

    place_order_button_locator = "//*[@id='order_form_content']/div[2]/button"

    # getters

    def get_location_name_locator(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.location_name_locator)))

    def get_location_popup_locator(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.location_popup_locator)))

    def get_popup_search_locator(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.popup_search_locator)))

    def get_popup_search_result_locator(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.popup_search_result_locator)))

    def get_close_popup_locator(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.close_popup_locator)))
        except TimeoutException:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.close_popup_locator)))

    def get_user_name_input_locator(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.user_name_input_locator)))

    def get_phone_input_locator(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.phone_input_locator)))

    def get_email_input_locator(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.email_input_locator)))

    def get_pay_in_cash_locator(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.pay_in_cash_locator)))

    def get_pay_by_card_locator(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.pay_by_card_locator)))

    def get_total_price_locator(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.total_price_locator)))

    def get_place_order_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.place_order_button_locator)))

    # actions

    @allure.step("Click location button")
    def click_location_button(self):
        self.get_location_name_locator().click()

    @allure.step("Enter location name")
    def enter_location_name(self, location_name):
        self.get_popup_search_locator().send_keys(location_name)

    @allure.step("Click location name")
    def click_location_name(self):
        self.get_popup_search_result_locator().click()

    @allure.step("Close location popup")
    def close_location_popup(self):
        try:
            self.get_close_popup_locator().click()
        except StaleElementReferenceException:
            self.get_close_popup_locator().click()
        except TimeoutException:
            self.get_close_popup_locator().click()

    @allure.step("Enter username")
    def enter_username(self, username):
        try:
            self.get_user_name_input_locator().send_keys(username)
        except StaleElementReferenceException:
            self.get_user_name_input_locator().send_keys(username)
        except ElementNotInteractableException:
            self.get_user_name_input_locator().send_keys(username)

    @allure.step("Enter phone number")
    def enter_phone_number(self,phone_number):
        try:
            self.get_phone_input_locator().send_keys(phone_number)
        except StaleElementReferenceException:
            self.get_phone_input_locator().send_keys(phone_number)
        except ElementNotInteractableException:
            self.get_phone_input_locator().send_keys(phone_number)

    @allure.step("Enter email")
    def enter_email(self,email):
        try:
            self.get_email_input_locator().send_keys(email)
        except StaleElementReferenceException:
            self.get_email_input_locator().send_keys(email)
        except ElementNotInteractableException:
            self.get_email_input_locator().send_keys(email)

    @allure.step("Click pay in cash button")
    def click_pay_in_cash(self):
        try:
            self.get_pay_in_cash_locator().click()
        except StaleElementReferenceException:
            self.get_pay_in_cash_locator().click()

    @allure.step("Click pay by card button")
    def click_pay_by_card(self):
        self.get_pay_by_card_locator()

    @allure.step("Click place order button")
    def click_place_order_button(self):
        self.get_place_order_button().click()

    @allure.step("Remove x1 from item's name")
    def remove_x(self, element):
        return element.split(" x1")[0]

    # methods

    @allure.step("Choose city")
    def choose_city(self):
        self.click_location_button()
        self.enter_location_name("Ижевск")
        self.click_location_name()
        self.close_location_popup()

    @allure.step("Enter user data")
    def enter_user_data(self):
        self.enter_username("Петров Пётр Петрович")
        self.enter_phone_number("89998885511")
        self.enter_email("test@test.net")

    @allure.step("Checking prices and names match")
    def compare_prices_and_names(self):
        self.click_pay_in_cash()
        time.sleep(5)
        # Приходится использовать time.sleep(), так как:
        # - Нет доступа к коду/API, чтобы отслеживать изменение цены явно.
        # - Цена обновляется асинхронно, и нет изменений в DOM для WebDriverWait.
        # - Эмпирически установлено, что 3 сек — минимальное стабильное время.
        sum = 0
        total_price = self.divide_price(self.get_total_price_locator().text)
        for i in range(1,count):
            item_name_getter = self.wait.until(EC.visibility_of_element_located(
                self.locator_maker(self.item_name_locator,i)))
            item_price_getter = self.wait.until(EC.visibility_of_element_located(
                self.locator_maker(self.item_price_locator,i)))

            item_name = self.remove_x(item_name_getter.text)
            item_price = self.divide_price(item_price_getter.text)

            assert Database.select_item_data(i)[0] == item_name
            assert Database.select_item_data(i)[1] == item_price
            sum += item_price
        assert sum == total_price
