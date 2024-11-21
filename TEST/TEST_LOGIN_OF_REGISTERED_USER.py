from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestUrl, TEST_USER
from locators import TestLocators
from conftest import driver


class TestLoginUsers:
    # Тестирование входа по кнопке "Войти в аккаунт" на главной странице
    def test_login_by_button_on_main(self, driver):
        driver.get(TestUrl.MAIN_URL_TEST)

        # Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        # Добавить ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        # Найти поле "Email" и заполнить
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(TEST_USER['email'])
        # Найти поле "Пароль" и заполнить его
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(TEST_USER['password'])
        # Найти и нажать кнопку "Войти"
        driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

        # Добавить ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
        )

        # Переход в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        assert driver.current_url == 'https://stellaburgers.nomoreparties.site/account/profile'

        # Тестирование входа через кнопку "Личный кабинет"
        def test_login_by_button_from_personal_account(self, driver):
            driver.get(TestUrl.MAIN_URL_TEST)

            # Находим кнопку "Личный кабинет" и нажать
            driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

            # Добавить ожидание для загрузки страницы
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    TestLocators.HEADER_FORM_LOGIN)
            )

            # Найти поле "Email" и заполнить его
            driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(TEST_USER['email'])
            # Найти поле "Пароль" и заполнить его
            driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(TEST_USER['password'])
            # Найти кнопку "Войти" и нажать
            driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

            # Добавить оджидание загрузки страницы
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    TestLocators.BUTTON_PLACE_AN_ORDER)
            )

            # Переходим в личный кабинет
            driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

            assert driver.current_url == 'https://stellaburgers.nomoreparties.site/account/profile'

            # Тестирование входа через кнопку в форме регистрации
            def test_login_by_button_from_registration_form(self, driver):
                driver.get(TestUrl.URL_REGISTRATION_FORM)

                # Найти кнопку "Войти" и нажать
                driver.find_element(*TestLocators.LOGIN_FROM_AUTORIZATION).click()

                # Добавить ожидание для загрузки страницы
                WebDriverWait(driver, 5).until(
                    expected_conditions.visibility_of_element_located(
                        TestLocators.HEADER_FORM_LOGIN)
                )

                # Найти поле "Email" и заполнить
                driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(TEST_USER['email'])
                # Найти поле "Пароль" и заполнить
                driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(TEST_USER['password'])
                # Найти и нажать кнопку "Войти"
                driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

                # Добавить ожидание для загрузки страницы
                WebDriverWait(driver, 5).until(
                    expected_conditions.visibility_of_element_located(
                        TestLocators.BUTTON_PLACE_AN_ORDER)
                )

                # Переходим в личный кабинет
                driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

                assert driver.current_url == 'https://stellaerburgers.nomoreparties.site/account/profile'

                # Тестирование вход чрез кнопку в форме восстановления пароля
                def test_login_by_button_from_psw_recovery_form(self, driver):
                    driver.get(TestUrl.URL_REGISTRATION_FORM)

                    # Найти кнопку "Войти" и нажать
                    driver.find_element(*TestLocators.LOGIN_FROM_RECOVERY_PSW).click()

                    # Найти поле "Email" и заполни его
                    driver.find_element(*TestLocators.LOGIN_FROM_RECOVERY_PSW).send_keys(TEST_USER['email'])

                    # Найти поле "Пароль" и заполнить его
                    driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(
                        TEST_USER['password'])
                    # Найти кнопку "Войти" и нажать
                    driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()
                    # Добавить ожидание для загрузки страницы
                    WebDriverWait(driver, 5).until(
                        expected_conditions.visibility_of_element_located(
                            TestLocators.BUTTON_PLACE_AN_ORDER)
                    )

                    # Переходим в личный кабинет
                    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

                    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'




