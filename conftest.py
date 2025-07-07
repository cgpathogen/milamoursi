import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from database.database import Database

@pytest.fixture(autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def create_database():
    Database.create_db()