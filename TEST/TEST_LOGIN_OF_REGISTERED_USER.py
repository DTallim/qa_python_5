from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import (testurl,test_user)
from locators import testlocators
from conftest import driver


class TestLoginUsers:
    def login_to_account(self,driver,start_url):
        driver.get(start_url)
        #Найти и нажать элемент для перехода к форме логина если необходимо
        if start_url == testurl.URL_REGISTRATION_FORM:
            driver.find_element(*testlocators.LOGIN_FROM_AUTORIZATION).click()
        elif start_url == testurl.URL_REGISTRATION_FORM:
            driver.find_element(*testlocators.LOGIN_FROM_RECOVERY_PSW).click()
        elif start_url == testurl.MAIN_URL_TEST:
            driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()
        elif start_url == testurl.MAIN_URL_TEST:
            driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        #Ожидание загрузки формы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(testlocators.HEADER_FORM_LOGIN)
        )

        #Заполенение формы логина

        driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(test_user['email'])
        driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(test_user['password'])
        driver.find_element(*testlocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

        #Ожидание загрузки страницы после логина
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(testlocators.BUTTON_PLACE_AN_ORDER)
        )


    # Тестирование входа по кнопке "Войти в аккаунт" на главной странице
    def test_login_by_button_on_main(self, driver):
        self.login_to_account(driver,testurl.MAIN_URL_TEST)
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_login_by_button_form_personal_account(self,driver):
        self.login_to_account(driver,testurl.MAIN_URL_TEST)
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
        assert driver.current_url =='https://stellarburgers.nomoreparties.site/account/profile'

    def test_login_by_button_from_registration_form(self,driver):
        self.login_to_account(driver, testurl.URL_REGISTRATION_FORM)
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
        assert  driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_login_by_button_from_psw_recovery_form(self,driver):
        self.login_to_account(driver,testurl.URL_PWS_RECOVERY_FORM)
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
