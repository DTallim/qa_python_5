from unittest import TextTestResult

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import testurl
from locators import testlocators
from conftest import driver

class TestFilterConstructor:
    #Тестирование перехода к разделу "Соусы"
    def test_go_to_section_cauces(self,driver):
        driver.get(testurl.MAIN_URL_TEST)

        #Найти и нажать на раздел "Соусы"
        driver.find_element(*testlocators.BUTTON_SAUCES).click()

       #Проверка, что элемент "Соусы" стал активным
        assert WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(testlocators.ACTIVE_BUTTON_SAUCES)
        )

        #тестирование перехода к разделу "Начинки"
        def test_go_to_section_fillings(self,driver):
            driver.get(testurl.MAIN_URL_TEST)

            #найти и нажать на раздел "Начинки"
            driver.find_element(*testlocators.BUTTON_FILLINGS).click()

            #Проверить, что элемент "Начинка" стал активным
            assert WebDriverWait(driver,5).until(
                expected_conditions.visibility_of_element_located(testlocators.ACTIVE_BUTTON_FILLENGS)
            )
        #Тестирование перехода к разделу "Булки"
        def test_go_to_section_buns(self,driver):
            driver.get(testurl.MAIN_URL_TEST)

            #Найти и нажать на раздел "Начинки"
            driver.find_element(*testlocators.BUTTON_FILLINGS).click()

            #Найти и нажать на раздел "Булки"
            driver.find_element(*testlocators.BUTTON_BUNS).click()

            #Проверить, что элемент "Булки" стол активным
            assert WebDriverWait(driver,5).until(
                expected_conditions.visibility_of_element_located(testlocators.ACTIVE_BUTTON_BUNS)
            )
