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

    # getters

    def get_search_input_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator_maker(self.search_input_button,1)))


    # actions

    def click_search_input_button(self):
        self.get_search_input_button().click()


    def open(self):
        """
        go to url's page
        """
        self.driver.get(self.page_url)