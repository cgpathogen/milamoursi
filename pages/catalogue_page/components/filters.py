import time

import allure

from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Filters(BasePage):

    @staticmethod
    def xpath_maker(text):
        """
        внутренний генератор xpath для опций фильтров
        """
        return f"//a[contains(text(),'{text}')]"

    dropdown_button_locator = "//a[@id='dropdownMenuButton']"
    dropdown_options_locator = "//div[@class='dropdown-menu custom-dropdown-item show']"

    sort_by_name_asc_locator = xpath_maker("по названию ⇑")
    sort_by_name_desc_locator = xpath_maker("по названию ⇓")
    sort_by_popular_asc_locator = xpath_maker("по популярности ⇑")
    sort_by_popular_desc_locator = xpath_maker("по популярности ⇓")
    sort_by_price_asc_locator = xpath_maker("по цене ⇑")
    sort_by_price_desc_locator = xpath_maker("по цене ⇓")

    # getters

    def get_dropdown_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.dropdown_button_locator)))

    def get_dropdown_options(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.dropdown_options_locator)))

    def get_sort_by_name_asc_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.sort_by_name_asc_locator)))

    def get_sort_by_name_desc_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.sort_by_name_desc_locator)))

    def get_sort_by_popular_asc_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.sort_by_popular_asc_locator)))

    def get_sort_by_popular_desc_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.sort_by_popular_desc_locator)))

    def get_sort_sort_by_price_asc_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.sort_by_price_asc_locator)))

    def get_sort_sort_by_price_desc_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.sort_by_price_desc_locator)))
