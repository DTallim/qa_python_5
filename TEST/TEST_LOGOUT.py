import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import testurl
from helpers import generates_email,generates_password
from locators import testlocators
from conftest import driver

class TestRegistration:
    #Тестирование формы регистрации с валидными данными "Email" и "Пароль"
    @pytest.mark.parametrize('email_char_num, psw_char_num,[(1,6),(2,7),(15,15)]')

    def test_registration_with_valid_email_and_password(self,driver,email_char_num,psw_char_num):

        driver.get(testurl.MAIN_URL_TEST)

        #Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        #Добавить явное ожидание для загрузки страницы
        wait = WebDriverWait(driver,5)
        wait.until(expected_conditions.presence_of_element_located(testlocators.HEADER_FORM_LOGIN))

        #Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*testlocators.HYPERTEXT_REGISTRATION).click()

        #Найти поле "Имя" и заполнить его
        driver.find_element(testlocators.INPUT_FORM_REGISTRATION_NAME).send_keys('Алиса')

        #Найти поле "Email" и заполнить его
        driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(generates_email(email_char_num))

        #Найти "Пароль" и заполнить его
        driver.find_element(*testlocators.BUTTON_REGISTRATION).click()

        #Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*testlocators.BUTTON_REGISTRATION).click()

        #Добавить ожидание для загрузки страницы
        wait.until(expected_conditions.presence_of_element_located(testlocators.HEADER_FORM_LOGIN))

        login_form = driver.find_element(*testlocators.HEADER_FORM_LOGIN)
        assert login_form.is_displayed(), "Форма входа в систему должна быть видна при успешной регистрации"
        assert driver.current_url == testurl.URL_LOGIN

    def test_registration_with_incorrect_psw(self,driver):
        driver.get(testurl.MAIN_URL_TEST)

        #Найти кнопку "Войти в аккаунт" и нажать
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()

        #Добавь явное ожидание для загрузки и нажать
        wait = WebDriverWait(driver,5)
        wait.until(expected_conditions.presence_of_element_located(testlocators.HEADER_FORM_LOGIN))

        #найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*testlocators.HYPERTEXT_REGISTRATION).click()

        #Найти поле "Имя" и заполнить
        driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_NAME).send_keys('Алиса')

        #Найти поле "Email" и заполнить
        driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(generates_email(5))

        #Найти поле "Пароль" и заполнить его
        driver.find_element(*testlocators.INPUT_FORM_REGISTRATION_PASSWORD).send_keys('qwe1')

        #Найти кнопку "Зарегистрироваться" и нажать
        driver.find_element(*testlocators.BUTTON_REGISTRATION).click()
        error_massage = wait.until(expected_conditions.presence_of_element_located(testlocators.INCORRECT_PASSWORD_MASSAGE))
        #Убедиться в появлении сообщения об ошибке
        assert error_massage.is_displayed(), "Должно быть видно сообщение об ошибке ввода пароля"




