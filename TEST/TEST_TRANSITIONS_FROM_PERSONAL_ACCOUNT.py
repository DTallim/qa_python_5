from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import test_url, test_user
from locators import testlocators
from conftest import driver

class TestTransitions:
    # Тестирование перехода из ЛК в конструктор
    def test_button_constructor(self, driver):
        driver.get(test_url.MAIN_URL_TEST)

        # Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.HEADER_FORM_LOGIN)
        )
        assert driver.find_element(*testlocators.HEADER_FORM_LOGIN).is_displayed(), "Форма логина не отображается"

        # Найти поле "Email" и заполни его
        driver.find_element(*testlocators.INPUT_FORM_AUTHORIZATIONS_EMAIL).send_keys(test_user['email'])
        # Найти поле "Пароль" и заполни его
        driver.find_element(*testlocators.INPUT_FORM_AUTHORIZATIONS_PASSWORD).send_keys(test_user['password'])
        # Найти кнопку "Войти" и нажать
        driver.find_element(*testlocators.BUTTON_FORM_AUTHORIZATIONS_LOGIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.BUTTON_PLACE_AN_ORDER)
        )
        assert driver.find_element(*testlocators.BUTTON_PLACE_AN_ORDER).is_displayed(), "Кнопка размещения заказа не отображается"

        # Переходим в личный кабинет
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.BUTTON_LOGOUT)
        )
        assert driver.find_element(
            *testlocators.BUTTON_LOGOUT).is_displayed(), "Кнопка выхода из аккаунта не отображается"

        # Найти "Конструктор" и нажать
        driver.find_element(*testlocators.BUTTON_CONSTRUCTOR).click()

        # Добавить явное ожидание
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.FORM_CONSTRUCTOR)
        )

    # Тестирование перехода из ЛК по Логотипу
    def test_logo_stellar_burgers (self, driver):
        driver.get(test_url.MAIN_URL_TEST)

        # Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.HEADER_FORM_LOGIN)
        )

        # Найти поле "Email" и заполни его
        driver.find_element(*testlocators.INPUT_FORM_AUTHORIZATIONS_EMAIL).send_keys(test_user['email'])
        # Найти поле "Пароль" и заполни его
        driver.find_element(*testlocators.INPUT_FORM_AUTHORIZATIONS_PASSWORD).send_keys(test_user['password'])
        # Найти кнопку "Войти" и нажать
        driver.find_element(*testlocators.BUTTON_FORM_AUTHORIZATIONS_LOGIN).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.BUTTON_PLACE_AN_ORDER)
        )

        # Переходим в личный кабинет
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.BUTTON_LOGOUT)
        )

        #Найти логотип и нажать
        driver.find_element(*testlocators.LOGO).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.BUTTON_PLACE_AN_ORDER)
        )

        assert driver.current_url == test_url.MAIN_URL_TEST
