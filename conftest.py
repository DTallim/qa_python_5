import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import testurl,test_user
from locators import testlocators

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.get(testurl.MAIN_URL_TEST)
    driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

    wait = WebDriverWait(driver,5)
    wait.until(expected_conditions.visibility_of_element_located(testlocators.HEADER_FORM_LOGIN))

    driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(test_user['email'])
    driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(test_user['password'])
    driver.find_element(*testlocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

    wait.until(expected_conditions.visibility_of_element_located(testlocators.BUTTON_PLACE_AN_ORDER))

    return driver
