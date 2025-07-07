import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
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
def prepare_database():
    if os.path.exists(Database.db_path):
        os.remove(Database.db_path)
    Database.create_db()