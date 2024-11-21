import pytest
from selenium import

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
