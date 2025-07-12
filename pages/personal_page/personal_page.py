import allure

from pages.base_page.base_page import BasePage
from pages.personal_page.components.sections import Sections

class PersonalCabinetPage(BasePage):

    page_url = "https://milamoursi.ru/personal"

    def __init__(self,driver):
        super().__init__(driver)
        self.sections = Sections(driver)
