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

        #Добавить явное ожидание подсвечивания элемента "Соусы"
        WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.ACTIVE_BUTTON_SAUCES)
        )

        #Находим изменения div
        update_class = testlocators.ACTIVE_BUTTON_SAUCES.get_attribute("class")

        assert driver.find_element(*testlocators.ACTIVE_BUTTON_SAUCES)

        #тестирование перехода к разделу "Начинки"
        def test_go_to_section_fillings(self,driver):
            driver.get(testurl.MAIN_URL_TEST)

            #найти и нажать на раздел "Начинки"
            driver.find_element(*testlocators.BUTTON_FILLINGS).click()

            #Добавить ожидание подсвечивания элемента "Начинки"
            WebDriverWait(driver,5).until(
                expected_conditions.visibility_of_element_located(
                    testlocators.ACTIVE_BUTTON_FILLENGS)
            )

            update_class=testlocators.ACTIVE_BUTTON_FILLENGS.get_attribute("class")

            assert driver.find_element(*testlocators.ACTIVE_BUTTON_FILLENGS)

        #Тестирование перехода к разделу "Булки"
        def test_go_to_section_buns(self,driver):
            driver.get(testurl.MAIN_URL_TEST)

            #Найти и нажать на раздел "Начинки"
            driver.find_element(*testlocators.BUTTON_FILLINGS).click()

            #Найти и нажать на раздел "Булки"
            driver.find_element(*testlocators.BUTTON_BUNS).click()

            #Добавить ожидание подсвечивания элемента "Начинки"
            WebDriverWait(driver,5).until(
                expected_conditions.visibility_of_element_located(
                    testlocators.ACTIVE_BUTTON_BUNS)
            )

            #
            update_class=testlocators.ACTIVE_BUTTON_BUNS.get_attribute("class")

            assert driver.find_element(*testlocators.ACTIVE_BUTTON_BUNS)
