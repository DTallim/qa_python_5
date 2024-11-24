from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import test_user, testurl
from locators import testlocators
from conftest import driver

class TestTransitions:
    # Тестирование перехода из ЛК в конструктор
    def test_button_constuctor(self,driver,login):
        driver = login

        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(testlocators.BUTTON_LOGOUT)
        )

        driver.find_element(*testlocators.BUTTON_CONSTRUCTOR).click()

        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(testlocators.FORM_CONSRTUCTOR)
        )

        constructor_element = driver.find_element(*testlocators.FORM_CONSRTUCTOR)
        assert constructor_element.is_displayed(), "Форма конструктора отображается"
        assert driver.current_url == testurl.MAIN_URL_TEST, "Перенаправлено на главную страницу с помощью конструктора"

    #Тестирование перехода из ЛК по Логотипу
    def test_logo_stellar_burgers(self,driver,login):
        driver = login

        driver.find_element(*testlocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(testlocators.BUTTON_LOGOUT)
        )

        order_button = WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(testlocators.BUTTON_PLACE_AN_ORDER)
        )

        assert order_button.is_displayed(), "Кнопка заказа должна быть видно на главной странице"
        assert driver.current_url == testurl.MAIN_URL_TEST, "Перенаправляет на главную станицу"

        constructor_form = driver.find_element(*testlocators.FORM_CONSRTUCTOR)
        assert constructor_form.is_displayed(), "Форма конструктора должна быть видна на главной странице"
