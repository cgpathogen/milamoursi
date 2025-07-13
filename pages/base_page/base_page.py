import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.common.exceptions import StaleElementReferenceException
from pages.base_page.components.nav_links import NavLinks

class BasePage:

    def __init__(self, driver):
        super().__init__(driver)
        self.nav_links = NavLinks(driver)
        self.driver : WebDriver = driver
        self.wait = WebDriverWait(driver,10,1)
        self.action = ActionChains(driver)


    # locators

    accept_cookie_btn = "//button[@id='nca-cookiesacceptpro-line-accept-btn']"
    search_input_button = "//div[@class='w-50']"
    input_field = "//input[@id='title-search-input-mobile']"
    user_options = "//ul[@class='navbar-nav flex-row justify-content-xl-end d-flex flex-wrap text-body py-0 navbar-right']/li"
    navbar_links = "//ul[@class='navbar-nav hover-menu main-menu px-0 mx-xl-n5']/li"
    add_to_cart_btn = "//a[@class='btn btn-secondary lh-12']"
    off_canvas_block = "//div[@class='canvas-sidebar cart-canvas show']"
    close_off_canvas = "//span[@class='canvas-close d-inline-block fs-24 mb-1 ml-auto lh-1 text-primary']"
    off_canvas_go_to_cart_locator = "//a[@class='btn btn-secondary btn-block mb-3']"



    # getters

    def get_accept_cookie_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.accept_cookie_btn)))

    def get_search_input_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.search_input_button,1)))

    def get_input_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.input_field)))

    def get_personal_account_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.user_options,1)))

    def get_favorites_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.user_options,2)))

    def get_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.user_options,3)))

    def get_off_canvas_block(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.off_canvas_block)))

    def get_close_off_canvas(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.close_off_canvas)))
        except StaleElementReferenceException:
            return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.close_off_canvas)))

    def get_off_canvas_go_to_cart_locator(self):
        return  self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.off_canvas_go_to_cart_locator)))

    # actions

    @allure.step("Accept cookie")
    def click_accept_cookie(self):
        self.get_accept_cookie_button().click()

    @allure.step("Click search input button")
    def click_search_input_button(self):
        self.get_search_input_button().click()

    @allure.step("Enter text")
    def enter_text(self, text):
        self.get_input_field().send_keys(f"{text}")
        self.get_input_field().send_keys(Keys.ENTER)

    @allure.step("Click personal account button")
    def click_personal_account_btn(self):
        self.get_personal_account_button().click()

    @allure.step("Click favorites button")
    def click_favorites_btn(self):
        self.get_favorites_button().click()

    @allure.step("Click cart button")
    def click_cart_button(self):
        try:
            self.get_cart_button().click()
        except StaleElementReferenceException:
            self.get_cart_button().click()

    @allure.step("Click off canvas menu button")
    def click_close_off_canvas_button(self):
        try:
            self.get_close_off_canvas().click()
        except StaleElementReferenceException:
            self.get_close_off_canvas().click()

    @allure.step("Click off-canvas menu go to cart button")
    def click_off_canvas_go_to_cart(self):
        self.get_off_canvas_go_to_cart_locator().click()


    # methods

    def locator_maker(self, xpath, index=None, option=None):
        """
        универсальный метод во избежание дублирования кода
        """
        if index is not None:
            return ("xpath",f"{xpath}[{index}]")
        if option is not None:
            return ("xpath", f"{xpath}[{index}]{option}")
        return ("xpath", xpath)

    @allure.step("scrolling page")
    def scroll(self,up, down):
        self.driver.execute_script(f"window.scrollBy({up}, {down});")


    def divide_price(self, price, old_price=False):
        """
        Метод для получения цены товара
        локатор в вёрстке не позволяет получить актуальную цену отдельно от старой цены, поэтому при её наличии
        срабатывает метод на отсечение старой цены
        Если старая цена отсутствует в блоке, то метод получает только актуальную цену
        """
        if old_price:
            return int(price.split("₽")[1].replace(" ", ""))
        else:
            return int(price.split("₽")[0].replace(" ", ""))


    def open(self):
        """
        переход на URL страницы
        """
        with allure.step(f"Open page {self.page_url}"):
            self.driver.get(self.page_url)