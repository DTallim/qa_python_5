from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import test_url
from locators import testlocators
from conftest import driver

class TestFilterConstructor:
    # Тестирование перехода к разделу "Соусы"
    def test_go_to_section_sauces(self, driver):
        driver.get(test_url.MAIN_URL_TEST)

        # Найти и нажать на раздел "Соусы"
        driver.find_element(*testlocators.BUTTON_SAUCES).click()

        active_sauces = WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.ACTIVE_BUTTON_SAUCES
            )
        )

        assert active_sauces.is_displayed()

    # Тестирование перехода к разделу "Начинки"
    def test_go_to_section_fillings(self, driver):
        driver.get(test_url.MAIN_URL_TEST)

        # Найти и нажать на раздел "Начинки"
        driver.find_element(*testlocators.BUTTON_FILLINGS).click()

        active_fillings = WebDriverWait(driver,5).until(
            expected_conditions.visibility_of_element_located(
                testlocatorsACTIVE_BUTTON_FILLINGS
            )
        )

        assert active_fillings.is_displayed()

    #Тестирование перехода к разделу "Булки"
    def test_go_to_section_buns(self, driver):
        driver.get(test_url.MAIN_URL_TEST)

        # Найти и нажать на раздел "Начинки"
        driver.find_element(*testlocators.BUTTON_FILLINGS).click()

        # Найти и нажать на раздел "Булки"
        driver.find_element(*testlocators.BUTTON_BUNS).click()

        # Добавить явное ожидание подсвечивания элемента "Начинки"
        active_buns = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                testlocators.ACTIVE_BUTTON_BUNS)
        )

        assert active_buns.is_displayed()
