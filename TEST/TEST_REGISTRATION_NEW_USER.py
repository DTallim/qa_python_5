import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import test_url
from helpers import generates_email, generates_password
from locators import testlocators
from conftest import driver

class TestRegistration:
    @pytest.mark.parametrize('email_char_num, psw_char_num',[[1,6], [2,7], [15,15]])
    def test_registration_with_valid_email_and_password(self,driver, email_char_num, psw_char_num):

        driver.get(test_url.MAIN_URL_TEST)

# Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
            testlocators.HEADER_FORM_LOGIN)
        )

# Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*testlocators.HYPERTEXT_REGISTRATION).click()

# Найти поле "Имя" и заполнить его
        driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_NAME).send_keys('Алисия')

# Найти поле "Email" и заполни его
        driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_EMAIL).send_keys(generates_email(email_char_num))

# Найти поле "Пароль" и заполни его
        driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_PASSWORD).send_keys(generates_password(psw_char_num))

# Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*testlocators.BUTTON_REGISTRATION).click()

# Добавь явное ожидание для загрузки страницы

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
            testlocators.HEADER_FORM_LOGIN)
        )

        assert driver.current_url == test_url.LOGIN_PAGE_URL

def test_registration_with_incorrect_psw(self, driver):
    driver.get(test_url.MAIN_URL_TEST)

# Найти кнопку "Войти в аккаунт" и нажать
    driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

# Добавь явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
        testlocators.HEADER_FORM_LOGIN)
    )

# Найти кнопку "Зарегистрироваться" и нажать
    driver.find_element(*testlocators.HYPERTEXT_REGISTRATION).click()

# Найти поле "Имя" и заполнить его
    driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_NAME).send_keys('Алисия')

# Найти поле "Email" и заполни его
    driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_EMAIL).send_keys(generates_email(5))

# Найти поле "Пароль" и заполни его
    driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_PASSWORD).send_keys('qw1')

# Найти кнопку "Зарегистрироваться" и нажать
    driver.find_element(*testlocators.BUTTON_REGISTRATION).click()

# Добавить явное ожидание для появления на странице сообщения об ошибке
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
        testlocators.INCORRECT_PASSWORD_MESSAGE)
    )

# Убедиться в появлении сообщения об ошибке
    assert driver.find_element(*testlocators.INCORRECT_PASSWORD_MESSAGE).is_displayed()