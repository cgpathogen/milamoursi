import time

import allure
from base.base_test import BaseTest

class TestPersonalCabinet(BaseTest):

    @allure.epic("User")
    @allure.story("Personal_cabinet")
    @allure.feature("Log in as unregistered user")
    def test_login_as_unregistered_user(self):
        """
        локатор алерта об отсутствии пользователя определяется только по индексу, имеет общий локатор с остальными инпутами
        и не позволяет использовать неявное ожидание, по этой причине используется time.sleep()
        """
        self.mainPage.open()
        self.mainPage.click_personal_account_btn()
        self.personalPage.enter_text_to_login_input(self.credentials.login)
        self.personalPage.enter_text_to_password_input(self.credentials.password)
        self.personalPage.click_login_button()
        time.sleep(1.5)
        assert self.personalPage.get_user_not_found_alert().text == "Такой пользователь не найден"