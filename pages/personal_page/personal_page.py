import allure

from pages.base_page.base_page import BasePage
from pages.personal_page.components.sections import Sections
from selenium.webdriver.support import expected_conditions as EC

class PersonalCabinetPage(BasePage):

    page_url = "https://milamoursi.ru/personal"

    def __init__(self,driver):
        super().__init__(driver)
        self.sections = Sections(driver)


    # locators

    login_input_locator = "//input[@name='PHONE_LOGIN_EMAIL']"
    password_input_locator = "//input[@name='PASSWORD']"
    login_button_locator = "(//button[@class='bxmaker-authuserphone-button'])[2]"
    user_not_found_locator = "//*[@id='bxmaker-authuserphone-enter__uB8qD7']/div[1]/div[3]/div[1]"

    # texts

    user_not_found_alert = "Такой пользователь не найден"
    no_login_entered_alert = "Не указан телефон, логин или email"
    no_password_entered_alert = "Не указан пароль"

    # getters

    def get_login_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.login_input_locator)))

    def get_password_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.password_input_locator)))

    def get_login_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.login_button_locator)))

    def get_user_not_found_alert(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.user_not_found_locator)))

    # actions

    @allure.step("Enter text to login input")
    def enter_text_to_login_input(self, login):
        self.get_login_input().send_keys(login)


    @allure.step("Enter text to password input")
    def enter_text_to_password_input(self, password):
        self.get_password_input().send_keys(password)


    @allure.step("Click login button")
    def click_login_button(self):
        self.get_login_button().click()