import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:

    def __init__(self, driver):
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
    dropdown_menu_locator = "//div[@class='dropdown-menu dropdown-menu-xl px-0 pb-10 pt-5 overflow-hidden x-animated x-fadeInUp dropdown-menu-listing show']"
    day_care_link_locator = "//*[@id='ihn4_menug8taYv']/li[4]/div/div/div/div[2]/ul/li[4]/a"
    bestsellers_link_locator = "(//a[@title='БЕСТСЕЛЛЕРЫ'])[1]"
    new_features_link_locator = "(//a[@title='НОВИНКИ'])[1]"
    sets_link_Locator = "(//a[@title='НАБОРЫ'])[1]"
    for_face_link_Locator = "(//a[@title='ДЛЯ ЛИЦА'])[1]"
    for_body_link_Locator = "(//a[@title='ДЛЯ ТЕЛА'])[1]"
    about_link_Locator = "(//a[@title='О БРЕНДЕ'])[1]"
    on_sale_link_Locator = "(//a[@title='АКЦИИ'])[1]"
    special_offers_link_locator = "(//a[@title='СПЕЦИАЛЬНЫЕ ПРЕДЛОЖЕНИЯ'])[1]"

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

    def get_dropdown_menu(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.dropdown_menu_locator)))

    def get_day_care_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.day_care_link_locator)))

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

    @allure.step("Hover for face link")
    def hover_for_face_link(self):
        self.action.move_to_element(self.get_for_face_link()).perform()

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

    @allure.step("Hover dropdown menu")
    def hover_dropdown_menu(self):
        self.action.move_to_element(self.get_dropdown_menu()).perform()

    @allure.step("Click day care link")
    def click_day_care_link(self):
        self.get_day_care_link().click()


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