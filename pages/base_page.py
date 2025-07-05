from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver : WebDriver = driver
        self.wait = WebDriverWait(driver,10,1)


    # locators

    def locator_maker(self,xpath,index=None):
        """
        to avoid code repeats when creating xpath locators
        """
        if index is not None:
            return ("xpath",f"{xpath}[{index}]")
        return ("xpath", xpath)

    search_input_button = "//div[@class='w-50']"
    user_options = "//ul[@class='navbar-nav flex-row justify-content-xl-end d-flex flex-wrap text-body py-0 navbar-right']/li"
    navbar_links = "//ul[@class='navbar-nav hover-menu main-menu px-0 mx-xl-n5']/li"

    # getters

    def get_search_input_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.search_input_button,1)))

    def get_personal_account_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.user_options,1)))


    def get_favorites_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.user_options,2)))


    def get_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.user_options,3)))


    # actions

    def click_search_input_button(self):
        self.get_search_input_button().click()


    def click_personal_account_btn(self):
        self.get_personal_account_button().click()


    def click_favorites_btn(self):
        self.get_favorites_button().click()


    def click_cart_button(self):
        self.get_cart_button().click()


    def open(self):
        """
        go to url's page
        """
        self.driver.get(self.page_url)