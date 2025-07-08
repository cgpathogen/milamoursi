from database.database import Database
from pages.base_page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from count import several_things_count

class SearchResultPage(BasePage):

    page_url = "https://milamoursi.ru/search/"

    # locators

    item_locator = "//div[@class='col-xl-3 col-lg-4 col-6']"
    add_to_cart_button_locator = "(//a[@class='btn btn-secondary lh-12'])"
    item_name_locator = "(//h2[@class='card-title fs-15 font-weight-500 mb-2'])"
    item_price_locator = "//*[@id='catalog']/div/div"

    # getters

    def get_item(self):
        """
        геттер для поиска первого в списке продукта
        для кейсов с покупкой нескольких товаров локаторы будут перебираться через цикл
        """
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.item_locator,1)))

    def get_add_to_cart_button(self):
        """
        геттер для клика по кнопке первого элемента
        для кейсов с покупкой нескольких товаров локаторы будут перебираться через цикл
        """
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.add_to_cart_button_locator,1)))

    def get_item_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.item_name_locator,1)))

    def get_item_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.item_price_locator,1)))

    # actions

    def hover_item(self):
        self.action.move_to_element(self.get_item()).perform()

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()


    # methods

    def add_several_items(self):
        """
        метод для добавления в корзину нескольких товаров
        веб-элементы задаются в этом методе отдельно от геттеров
        и перебираются через цикл for в диапазоне числа из several_things_count
        некоторые локаторы на сайте дублируются независимо от локатора родительского элемента
        (индекс 1,2 для десктоп-версии, 3,4 - для мобильной версии и тд)
        поэтому создана переменная n, которая с каждой итерацией увеличивается на 2, чтобы нажать соответствующую кнопку
        """
        n = 1
        for i in range(1, several_things_count):
            # inner locators
            item = self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.item_locator, i)))
            add_button = EC.element_to_be_clickable(self.locator_maker(self.add_to_cart_button_locator, n))
            item_name = self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.item_name_locator,i)))
            item_price = self.wait.until(EC.visibility_of_element_located(self.locator_maker(self.item_price_locator,i,"/div/div[2]/p/span[2]")))
            # get price
            get_price = self.divide_price(item_price.text,True)
            # main algorythm
            self.action.move_to_element(item).perform()
            self.wait.until(add_button).click()
            self.click_close_off_canvas_button()
            Database.update_data(item_name.text, get_price)
            n += 2