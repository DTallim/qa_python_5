from xml.sax.saxutils import escape

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestUrl, TEST_USER
from locators import TestLocators
from conftest import driver

class TestTransitions:
    # Тестирование перехода из ЛК в конструктор
    def test_button_constuctor(self,driver):
        driver.get(TestUrl.MAIN_URL_TEST)

    #найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

    #Добавь ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
    )

    #Найти поле "Email" и заполнить
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(TEST_USER['email'])

    #Найти поле "Пароль" и заполнить его
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(TEST_USER['password'])

    #Найти поле "Войти" и нажать
        driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

    #Добавить ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
    )

    #Переходим в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_LOGOUT)
    )

    #Найти "Конструктор" и нажать
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()

    #Добавить явное ожидание
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.FORM_CONSRTUCTOR)
    )

        assert driver.find_element(*TestLocators.FORM_CONSRTUCTOR)

    #Тестирование перехода из ЛК по Логотипу
    def test_logo_stellar_burgers(self,driver):
        driver.get(TestUrl.MAIN_URL_TEST)

        #Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        #Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        #Найти поле "email" и заполни его
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(TEST_USER['email'])
        #Найти поле "Пароль" и заполнить его
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(TEST_USER['password'])
        #Найти кнопку "Войти" и нажать
        driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

        #Добавь ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
        )

        #Переходим в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_LOGOUT)
        )

        #Найти логотип и нажать
        driver.find_element(*TestLocators.LOGO).click()

        #Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
        )

        assert driver.current_url == 'https://stellarbubgers.nomorepatries.site/'