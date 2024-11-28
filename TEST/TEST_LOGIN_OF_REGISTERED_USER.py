from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import test_url, test_user
from locators import testlocators
from conftest import driver


def login_user(driver):
    WebDriverWait(driver,10).until(
        expected_conditions.visibility_of_element_located(
            testlocators.HEADER_FORM_LOGIN
        )
    )
    driver.find_element(*testlocators.INPUT_FORM_AUTHORIZATIONS_EMAIL).send_keys(test_user['email'])
    driver.find_element(*testlocators.INPUT_FORM_AUTHORIZATIONS_PASSWORD).send_keys(test_user['password'])

    driver.find_element(*testlocators.BUTTON_FORM_AUTHORIZATIONS_LOGIN).click()

    WebDriverWait(driver,10).until(
        expected_conditions.visibility_of_element_located(
            testlocators.BUTTON_PLACE_AN_ORDER
        )
    )

    driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'


class TestLoginUsers:
    # Тестирование входа по кнопке «Войти в аккаунт» на главной
    def test_login_by_button_on_main(self,driver):
        driver.get(test_url.MAIN_URL_TEST)

        # Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()
        login_user(driver)

    # Тестирование входа через кнопку «Личный кабинет»
    def test_login_by_button_from_personal_account(self,driver):
        driver.get(test_url.MAIN_URL_TEST)

        # Находим кнопку "Личный кабинет" и нажать
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
        login_user(driver)

    # Тестирование входа через кнопку в форме регистрации
    def test_login_by_button_from_registration_form(self, driver):
        driver.get(test_url.URL_REGISTRATION_FORM)

        # Найти кнопку "Войти" и нажать
        driver.find_element(*testlocators.LOGIN_FROM_AUTHORIZATIONS).click()
        login_user(driver)

    # Тестирование вход через кнопку в форме восстановления пароля
    def test_login_by_button_from_psw_recovery_form (self, driver):
        driver.get(test_url.URL_PSW_RECOVERY_FORM)

        # Найти кнопку "Войти" и нажать
        driver.find_element(*testlocators.LOGIN_FROM_RECOVERY_PSW).click()
        login_user(driver)
