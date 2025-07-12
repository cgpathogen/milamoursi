import time

import allure
from base.base_test import BaseTest

class TestPersonalCabinet(BaseTest):

    @allure.epic("User")
    @allure.story("Personal_cabinet")
    def test_personal_cabinet(self):
        self.mainPage.open()
        self.mainPage.click_personal_account_btn()
        self.personalPage.sections.click_personal_data()
        time.sleep(3)