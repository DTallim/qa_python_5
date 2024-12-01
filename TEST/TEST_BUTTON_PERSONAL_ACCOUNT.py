from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import test_url, test_user
from locators import testlocators
from conftest import driver

class TestButtonPersAcc:
    def authorize(self,driver):
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()
        WebDriverWait(driver,10).until(
            expected_conditions.visibility_of_element_located(
                testlocators.HEADER_FORM_LOGIN)
        )

        driver.find_element(*testlocators.INPUT_FORM_AUTHORIZATIONS_EMAIL).send_keys(test_user['email'])
        driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_PASSWORD).send_keys(test_user['password'])
        driver.find_element(*testlocators.BUTTON_FORM_AUTHORIZATIONS_LOGIN).click()

        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.BUTTON_PLACE_AN_ORDER
            )
        )


    # Тестирование перехода авторизованного пользователя
    def test_click_button_autorized_user(self,driver):
        driver.get(test_url.MAIN_URL_TEST)

        self.authorize(driver)

        # Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        profile_element = WebDriverWait(driver,5).until(
            expected_conditions.presence_of_element_located(
                testlocators.PROFILE_SECTION
            )
        )
        assert profile_element is not None, "Элемент профиля не найден"

    # Тестирование перехода не авторизованного пользователя
    def test_click_button_unautorized_user(self,driver):
        driver.get(test_url.MAIN_URL_TEST)

        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        login_form = WebDriverWait(driver,5).until(
            expected_conditions.presence_of_element_located(
                testlocators.HEADER_FORM_LOGIN
            )
        )

        assert login_form is not None, "Форма входа не найдена"