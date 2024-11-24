from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import testurl,test_user
from locators import testlocators
from conftest import driver


class TestLoginUsers:
    def wait_for_element(self,driver,locator,timeout=5):
        return WebDriverWait(driver,timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
    def login_user(self,driver):
        self.wait_for_element(driver, testlocators.HEADER_FORM_LOGIN)

        driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(test_user['email'])
        driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(test_user['password'])
        driver.find_element(*testlocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

        self.wait_for_element(driver,testlocators.BUTTON_PLACE_AN_ORDER)
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        assert driver.current_url ==testurl.URL_PROFILE


    # Тестирование входа по кнопке "Войти в аккаунт" на главной странице
    def test_login_by_button_on_main(self, driver):
        driver.get(testurl.MAIN_URL_TEST)
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()
        self.login_user(driver)

    def test_login_by_button_form_personal_account(self,driver):
       driver.get(testurl.MAIN_URL_TEST)
       driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
       self.login_user(driver)

    def test_login_by_button_from_registration_form(self,driver):
       driver.get(testurl.MAIN_URL_TEST)
       driver.find_element(*testlocators.LOGIN_FROM_AUTORIZATION).click()
       self.login_user(driver)

    def test_login_by_button_from_psw_recovery_form(self,driver):
        driver.get(testurl.URL_PWS_RECOVERY_FORM)
        driver.find_element(*testlocators.LOGIN_FROM_RECOVERY_PSW).click()
        self.login_user(driver)


