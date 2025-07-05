from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver):
        self.driver : WebDriver = driver


    def open(self):
        """
        go to url's page
        """
        self.driver.get(self.page_url)