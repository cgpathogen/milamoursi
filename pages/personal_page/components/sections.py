import allure

from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class Sections(BasePage):

    # locators

    origin_locator = "//*[@id='content']/section[2]/div/div/div[1]/div/ul/li"
    personal_data_locator = origin_locator + "[1]/a"
    addresses_locator = origin_locator + "[2]/a"
    orders_locator = origin_locator + "[3]/a"
    favourites_locator = orders_locator + "[4]/a"
    logout_locator = origin_locator + "[5]/a"

    # getters

    def get_personal_data(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.personal_data_locator)))
        except StaleElementReferenceException:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.personal_data_locator)))

    def get_addresses(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.addresses_locator)))
        except StaleElementReferenceException:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.addresses_locator)))

    def get_orders(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.orders_locator)))
        except StaleElementReferenceException:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.orders_locator)))

    def get_favourites(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.favourites_locator)))
        except StaleElementReferenceException:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.favourites_locator)))

    def get_logout(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.logout_locator)))
        except StaleElementReferenceException:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.logout_locator)))

    # actions

    @allure.step("Click personal data link")
    def click_personal_data(self):
        self.get_personal_data().click()

    @allure.step("Click addresses link")
    def click_addresses(self):
        self.get_addresses().click()

    @allure.step("Click orders link")
    def click_orders(self):
        self.get_orders().click()

    @allure.step("Click favourites link")
    def click_favourites(self):
        self.get_favourites().click()

    @allure.step("Click logout link")
    def click_logout(self):
        self.get_logout().click()