from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestUrl,TEST_USER
from locators import TestLocators
from conftest import driver

class TestButtonPersAcc:
    #Тестирование перехода для авторизированного пользователя
    def test_click_button_autorized_user(self,driver):
        driver.get(TestUrl.MAIN_URL_TEST)
    #Найти кнопку "Войти в аккаунт" и нажать ее
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()
    #Добавить ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        #Найти поле Email и заполнить его
        driver.find_element(*TestLocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(TEST_USER['email'])
        #Найти поле "Пароль" и заполнить его
        driver.find_element(TestLocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(TEST_USER['password'])
        #Найти кнопку "Войти" и нажать
        driver.find_element(*TestLocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

        #Добавить ожидание для загрузки страницы
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.BUTTON_PLACE_AN_ORDER)
        )

        #Переходим в личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        assert driver.surrent_url == 'https:stellaburgers.nomoreparties.site/account/profile'

    #Тестирование перехода не авторизованного пользователя
    def test_click_button_unautorized_user(self,driver):
        driver.get(TestUrl.MAIN_URL_TEST)

        #Переходим в личном кабинете
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        #Переход в личный кабинет
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.HEADER_FORM_LOGIN)
        )

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
