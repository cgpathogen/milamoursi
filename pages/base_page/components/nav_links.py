import allure

from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class NavLinks(BasePage):

    # locators

    bestsellers_link_locator = "(//a[@title='БЕСТСЕЛЛЕРЫ'])[1]"
    new_features_link_locator = "(//a[@title='НОВИНКИ'])[1]"
    sets_link_Locator = "(//a[@title='НАБОРЫ'])[1]"
    for_face_link_Locator = "(//a[@title='ДЛЯ ЛИЦА'])[1]"
    for_body_link_Locator = "(//a[@title='ДЛЯ ТЕЛА'])[1]"
    about_link_Locator = "(//a[@title='О БРЕНДЕ'])[1]"
    on_sale_link_Locator = "(//a[@title='АКЦИИ'])[1]"
    special_offers_link_locator = "(//a[@title='СПЕЦИАЛЬНЫЕ ПРЕДЛОЖЕНИЯ'])[1]"


    # getters

    def get_bestsellers_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.bestsellers_link_locator)))

    def get_new_features_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.new_features_link_locator)))

    def get_new_sets_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.sets_link_Locator)))

    def get_for_face_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.for_face_link_Locator)))

    def get_for_body_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.for_body_link_Locator)))

    def get_about_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.about_link_Locator)))

    def get_on_sale_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.on_sale_link_Locator)))

    def get_special_offers_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.special_offers_link_locator)))


    # actions

    @allure.step("Click bestsellers link")
    def click_bestsellers_link(self):
        self.get_bestsellers_link().click()

    @allure.step("Click new features link")
    def click_new_features_link(self):
        self.get_new_features_link().click()

    @allure.step("Click new sets link")
    def click_new_sets_link(self):
        self.get_new_sets_link().click()

    @allure.step("Click for face link")
    def click_for_face_link(self):
        self.get_for_face_link().click()

    @allure.step("Click for body link")
    def click_for_body_link(self):
        self.get_for_body_link().click()

    @allure.step("Click about link")
    def click_about_link(self):
        self.get_about_link().click()

    @allure.step("Click on_sale link")
    def click_on_sale_link(self):
        self.get_on_sale_link().click()

    @allure.step("Click special_offers link")
    def click_special_offers_link(self):
        self.get_special_offers_link().click()