from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import testurl,test_user
from locators import testlocators
from conftest import driver

class TestButtonPersAcc:
    #Тестирование перехода для авторизированного пользователя
    def test_click_button_autorized_user(self,driver):
        driver.get(testurl.MAIN_URL_TEST)
    #Найти кнопку "Войти в аккаунт" и нажать ее
        driver.find_element(*testlocators.BUTTON_LOGIN_IN_ACC_IN_MAIN).click()
    #Добавить ожидание для загрузки страницы
        wait = WebDriverWait(driver,5)
        wait.until(expected_conditions.visibility_of_element_located(testlocators.HEADER_FORM_LOGIN))

        #Найти поле Email и заполнить его
        driver.find_element(*testlocators.INPUT_FROM_AUTORIZATIONS_EMAIL).send_keys(test_user['email'])
        #Найти поле "Пароль" и заполнить его
        driver.find_element(testlocators.INPUT_FROM_AUTORIZATIONS_PASSWORD).send_keys(test_user['password'])
        #Найти кнопку "Войти" и нажать
        driver.find_element(*testlocators.BUTTON_FORM_AUTORIZATIONS_LOGIN).click()

        #Добавить ожидание для загрузки страницы
        wait.until(expected_conditions.visibility_of_element_located(testlocators.BUTTON_PLACE_AN_ORDER))

        #Переходим в личный кабинет
        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        profile_url = testurl.URL_PROFILE
        wait.until(expected_conditions.url_to_be(profile_url))
        assert driver.current_url == profile_url, "Должен быть перенаправлен на страницу профиля"

    #Тестирование перехода не авторизованного пользователя
    def test_click_button_unautorized_user(self,driver):
        driver.get(testurl.MAIN_URL_TEST)

        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()

        wait = WebDriverWait(driver,5)
        wait.until(expected_conditions.visibility_of_element_located(testlocators.HEADER_FORM_LOGIN))

        login_url = testurl.URL_LOGIN
        wait.until(expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url,"Должен перенаправить на страницу входа в систему"

        login_header = driver.find_element(*testlocators.HEADER_FORM_LOGIN)
        assert login_header.is_displayed(), "Форма входа в систему должны быть видна"
